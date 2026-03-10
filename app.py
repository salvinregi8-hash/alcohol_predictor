import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
import warnings
warnings.filterwarnings('ignore')

# Page config
st.set_page_config(page_title="Beer Servings Prediction", layout="wide")

# Title
st.title("🍺 Beer Servings Prediction App")
st.write("Predict total alcohol consumption based on beverage servings")

# Load data
@st.cache_data
def load_data():
    try:
        df = pd.read_csv('data/beer-servings.csv')
    except:
        # Sample data if file not found
        df = pd.DataFrame({
            'Country': ['Brazil', 'USA', 'China', 'India', 'Russia', 'Germany', 'France', 'Japan', 'UK', 'Canada'] * 14,
            'Beer_servings': np.random.randint(0, 400, 140),
            'Spirit_servings': np.random.randint(0, 300, 140),
            'Wine_servings': np.random.randint(0, 370, 140),
            'Continent': np.random.choice(['Africa', 'Asia', 'Europe', 'North America', 'South America', 'Oceania'], 140),
            'total_litres_of_pure_alcohol': np.random.uniform(0, 15, 140)
        })
    return df

@st.cache_resource
def train_models(df):
    # Prepare data
    X = df[['Beer_servings', 'Spirit_servings', 'Wine_servings']].copy()
    
    # Encode categorical
    le_country = LabelEncoder()
    le_continent = LabelEncoder()
    
    X['Country'] = le_country.fit_transform(df['Country'])
    X['Continent'] = le_continent.fit_transform(df['Continent'])
    
    y = df['total_litres_of_pure_alcohol']
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Scale
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Model 1: Linear Regression
    lr = LinearRegression()
    lr.fit(X_train_scaled, y_train)
    lr_pred = lr.predict(X_test_scaled)
    lr_r2 = r2_score(y_test, lr_pred)
    lr_rmse = np.sqrt(mean_squared_error(y_test, lr_pred))
    
    # Model 2: Random Forest
    rf = RandomForestRegressor(n_estimators=100, random_state=42, max_depth=10)
    rf.fit(X_train_scaled, y_train)
    rf_pred = rf.predict(X_test_scaled)
    rf_r2 = r2_score(y_test, rf_pred)
    rf_rmse = np.sqrt(mean_squared_error(y_test, rf_pred))
    
    # Choose best
    if rf_r2 > lr_r2:
        best_model = rf
        best_name = "Random Forest"
        best_r2 = rf_r2
        best_rmse = rf_rmse
    else:
        best_model = lr
        best_name = "Linear Regression"
        best_r2 = lr_r2
        best_rmse = lr_rmse
    
    return {
        'best_model': best_model,
        'scaler': scaler,
        'le_country': le_country,
        'le_continent': le_continent,
        'best_name': best_name,
        'best_r2': best_r2,
        'best_rmse': best_rmse,
        'lr_r2': lr_r2,
        'lr_rmse': lr_rmse,
        'rf_r2': rf_r2,
        'rf_rmse': rf_rmse
    }

# Load data
df = load_data()

# Sidebar menu
page = st.sidebar.radio("📋 Select Page", ["📊 Dashboard", "🔮 Prediction", "📈 Performance"])

if page == "📊 Dashboard":
    st.header("Dashboard")
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Countries", len(df['Country'].unique()))
    col2.metric("Avg Beer Servings", f"{df['Beer_servings'].mean():.1f}")
    col3.metric("Avg Spirit Servings", f"{df['Spirit_servings'].mean():.1f}")
    col4.metric("Avg Wine Servings", f"{df['Wine_servings'].mean():.1f}")
    
    st.divider()
    
    # Simple tables instead of charts
    st.subheader("Data by Continent")
    continent_stats = df.groupby('Continent').agg({
        'Beer_servings': 'mean',
        'Spirit_servings': 'mean',
        'Wine_servings': 'mean',
        'total_litres_of_pure_alcohol': 'mean'
    }).round(2)
    st.table(continent_stats)
    
    st.subheader("Sample Data")
    st.dataframe(df.head(10), use_container_width=True)

elif page == "🔮 Prediction":
    st.header("Make a Prediction")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Input Values")
        beer = st.number_input("Beer Servings", 0, 500, 100)
        spirit = st.number_input("Spirit Servings", 0, 400, 50)
        wine = st.number_input("Wine Servings", 0, 400, 30)
        country = st.selectbox("Country", sorted(df['Country'].unique()))
        continent = st.selectbox("Continent", sorted(df['Continent'].unique()))
    
    with col2:
        st.subheader("Prediction Result")
        
        # Train model
        models = train_models(df)
        
        # Make prediction
        le_country = models['le_country']
        le_continent = models['le_continent']
        scaler = models['scaler']
        best_model = models['best_model']
        
        try:
            country_enc = le_country.transform([country])[0]
            continent_enc = le_continent.transform([continent])[0]
            
            input_data = np.array([[beer, spirit, wine, country_enc, continent_enc]])
            input_scaled = scaler.transform(input_data)
            prediction = best_model.predict(input_scaled)[0]
            
            st.metric("Predicted Alcohol (Litres)", f"{prediction:.2f}")
            st.info(f"Model: {models['best_name']}\nR² Score: {models['best_r2']:.4f}")
            
            # Show actual if available
            actual = df[df['Country'] == country]['total_litres_of_pure_alcohol'].values
            if len(actual) > 0:
                st.success(f"Actual for {country}: {actual[0]:.2f} L")
        except Exception as e:
            st.error(f"Error: {str(e)}")

elif page == "📈 Performance":
    st.header("Model Performance")
    
    models = train_models(df)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("Linear Regression")
        st.metric("R² Score", f"{models['lr_r2']:.4f}")
        st.metric("RMSE", f"{models['lr_rmse']:.4f}")
    
    with col2:
        st.subheader("Random Forest")
        st.metric("R² Score", f"{models['rf_r2']:.4f}")
        st.metric("RMSE", f"{models['rf_rmse']:.4f}")
    
    with col3:
        st.subheader("Best Model ⭐")
        st.metric("Model", models['best_name'])
        st.metric("R² Score", f"{models['best_r2']:.4f}")
        st.metric("RMSE", f"{models['best_rmse']:.4f}")
    
    st.divider()
    st.info("✓ Model trained on 80% of data\n✓ Evaluated on 20% of data\n✓ Features scaled with StandardScaler\n✓ Best model selected by R² score")
