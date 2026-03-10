import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
import warnings
warnings.filterwarnings('ignore')

# Page configuration
st.set_page_config(
    page_title="Beer Servings Prediction",
    page_icon="🍺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main-header {
        text-align: center;
        color: #D4AF37;
        font-size: 2.5em;
        margin-bottom: 1em;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin: 10px 0;
    }
    </style>
""", unsafe_allow_html=True)

# Load and prepare data
@st.cache_data
def load_data():
    """Load and preprocess beer servings data"""
    try:
        df = pd.read_csv('data/beer-servings.csv')
    except:
        # Create sample data if file not found
        df = pd.DataFrame({
            'Country': ['Brazil', 'USA', 'China', 'India', 'Russia', 'Germany', 'France', 'Japan', 'UK', 'Canada'] * 10,
            'Beer_servings': np.random.randint(0, 400, 100),
            'Spirit_servings': np.random.randint(0, 300, 100),
            'Wine_servings': np.random.randint(0, 370, 100),
            'Continent': np.random.choice(['Africa', 'Asia', 'Europe', 'North America', 'South America', 'Oceania'], 100),
            'total_litres_of_pure_alcohol': np.random.uniform(0, 15, 100)
        })
    return df

@st.cache_resource
def train_models(df):
    """Train and return best model"""
    # Prepare data
    X = df[['Beer_servings', 'Spirit_servings', 'Wine_servings']].copy()
    
    # Encode categorical variables
    le_country = LabelEncoder()
    le_continent = LabelEncoder()
    
    X['Country'] = le_country.fit_transform(df['Country'])
    X['Continent'] = le_continent.fit_transform(df['Continent'])
    
    y = df['total_litres_of_pure_alcohol']
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Model 1: Linear Regression
    lr_model = LinearRegression()
    lr_model.fit(X_train_scaled, y_train)
    lr_pred = lr_model.predict(X_test_scaled)
    lr_r2 = r2_score(y_test, lr_pred)
    lr_rmse = np.sqrt(mean_squared_error(y_test, lr_pred))
    
    # Model 2: Random Forest
    rf_model = RandomForestRegressor(n_estimators=100, random_state=42, max_depth=10)
    rf_model.fit(X_train_scaled, y_train)
    rf_pred = rf_model.predict(X_test_scaled)
    rf_r2 = r2_score(y_test, rf_pred)
    rf_rmse = np.sqrt(mean_squared_error(y_test, rf_pred))
    
    # Hyperparameter tuning for Random Forest
    best_rf = RandomForestRegressor(n_estimators=150, max_depth=12, min_samples_split=5, 
                                     min_samples_leaf=2, random_state=42)
    best_rf.fit(X_train_scaled, y_train)
    best_rf_pred = best_rf.predict(X_test_scaled)
    best_rf_r2 = r2_score(y_test, best_rf_pred)
    best_rf_rmse = np.sqrt(mean_squared_error(y_test, best_rf_pred))
    
    # Choose best model
    if best_rf_r2 >= lr_r2 and best_rf_r2 >= rf_r2:
        best_model = best_rf
        best_r2 = best_rf_r2
        best_rmse = best_rf_rmse
        model_name = "Random Forest (Tuned)"
    elif rf_r2 >= lr_r2:
        best_model = rf_model
        best_r2 = rf_r2
        best_rmse = rf_rmse
        model_name = "Random Forest"
    else:
        best_model = lr_model
        best_r2 = lr_r2
        best_rmse = lr_rmse
        model_name = "Linear Regression"
    
    return {
        'best_model': best_model,
        'scaler': scaler,
        'le_country': le_country,
        'le_continent': le_continent,
        'best_r2': best_r2,
        'best_rmse': best_rmse,
        'model_name': model_name,
        'lr_r2': lr_r2,
        'lr_rmse': lr_rmse,
        'rf_r2': rf_r2,
        'rf_rmse': rf_rmse,
        'X_test': X_test,
        'y_test': y_test
    }

# Main app
def main():
    st.markdown('<h1 class="main-header">🍺 Beer Servings & Alcohol Consumption Prediction</h1>', unsafe_allow_html=True)
    
    # Load data
    df = load_data()
    
    # Navigation
    page = st.sidebar.radio("Navigation", ["📊 Dashboard", "🔮 Prediction", "📈 Model Performance"])
    
    if page == "📊 Dashboard":
        show_dashboard(df)
    elif page == "🔮 Prediction":
        models_data = train_models(df)
        show_prediction(models_data, df)
    else:
        models_data = train_models(df)
        show_performance(models_data)

def show_dashboard(df):
    """Display data infographics"""
    st.header("Data Overview & Infographics")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Countries", len(df['Country'].unique()))
    with col2:
        st.metric("Avg Beer Servings", f"{df['Beer_servings'].mean():.1f}")
    with col3:
        st.metric("Avg Spirit Servings", f"{df['Spirit_servings'].mean():.1f}")
    with col4:
        st.metric("Avg Wine Servings", f"{df['Wine_servings'].mean():.1f}")
    
    st.divider()
    
    # Visualizations
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Beer Servings by Continent")
        fig1 = px.bar(df.groupby('Continent')['Beer_servings'].mean().reset_index(),
                      x='Continent', y='Beer_servings',
                      title="Average Beer Servings by Continent",
                      color='Beer_servings',
                      color_continuous_scale='Blues')
        st.plotly_chart(fig1, use_container_width=True)
    
    with col2:
        st.subheader("Alcohol Distribution")
        fig2 = px.pie(df, names='Continent', values='total_litres_of_pure_alcohol',
                      title="Total Alcohol Consumption by Continent")
        st.plotly_chart(fig2, use_container_width=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Alcohol vs Beer Servings")
        fig3 = px.scatter(df, x='Beer_servings', y='total_litres_of_pure_alcohol',
                         color='Continent', hover_data=['Country'],
                         title="Correlation: Beer Servings vs Total Alcohol")
        st.plotly_chart(fig3, use_container_width=True)
    
    with col2:
        st.subheader("Servings Distribution")
        fig4 = px.box(df, y=['Beer_servings', 'Spirit_servings', 'Wine_servings'],
                      title="Distribution of Beverage Types",
                      points="outliers")
        st.plotly_chart(fig4, use_container_width=True)
    
    # Data table
    st.subheader("Dataset Sample")
    st.dataframe(df.head(10), use_container_width=True)

def show_prediction(models_data, df):
    """Show prediction interface"""
    st.header("🔮 Predict Total Alcohol Consumption")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Input Features")
        
        # Numerical inputs
        beer_servings = st.number_input(
            "Beer Servings",
            min_value=0, max_value=500, value=100, step=10,
            help="Average servings of beer consumed per year"
        )
        
        spirit_servings = st.number_input(
            "Spirit Servings",
            min_value=0, max_value=400, value=50, step=10,
            help="Average servings of spirits consumed per year"
        )
        
        wine_servings = st.number_input(
            "Wine Servings",
            min_value=0, max_value=400, value=30, step=10,
            help="Average servings of wine consumed per year"
        )
        
        # Dropdown for country
        country = st.selectbox(
            "Country",
            options=sorted(df['Country'].unique()),
            help="Select a country"
        )
        
        # Dropdown for continent
        continent = st.selectbox(
            "Continent",
            options=sorted(df['Continent'].unique()),
            help="Select a continent"
        )
    
    # Prepare input for prediction
    le_country = models_data['le_country']
    le_continent = models_data['le_continent']
    scaler = models_data['scaler']
    best_model = models_data['best_model']
    
    try:
        country_encoded = le_country.transform([country])[0]
        continent_encoded = le_continent.transform([continent])[0]
        
        input_features = np.array([[beer_servings, spirit_servings, wine_servings, 
                                   country_encoded, continent_encoded]])
        input_scaled = scaler.transform(input_features)
        prediction = best_model.predict(input_scaled)[0]
        
        with col2:
            st.subheader("Prediction Result")
            
            # Display prediction with nice formatting
            st.markdown(f"""
                <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                            padding: 30px; border-radius: 10px; color: white; text-align: center;">
                    <h3>Predicted Total Alcohol (Litres)</h3>
                    <h1 style="font-size: 3em; margin: 0;">{prediction:.2f} L</h1>
                </div>
            """, unsafe_allow_html=True)
            
            st.divider()
            st.info(f"Model Used: **{models_data['model_name']}**\nR² Score: **{models_data['best_r2']:.4f}**")
            
            # Comparison with similar countries
            similar = df[(df['Country'] == country)]
            if len(similar) > 0:
                actual = similar['total_litres_of_pure_alcohol'].values[0]
                st.success(f"Actual value for {country}: **{actual:.2f} L**")
                st.caption(f"Prediction error: {abs(prediction - actual):.2f} L")
    
    except Exception as e:
        st.error(f"Error in prediction: {str(e)}")

def show_performance(models_data):
    """Show model performance metrics"""
    st.header("📈 Model Performance Comparison")
    
    col1, col2, col3 = st.columns(3)
    
    # Linear Regression
    with col1:
        st.subheader("Linear Regression")
        st.metric("R² Score", f"{models_data['lr_r2']:.4f}")
        st.metric("RMSE", f"{models_data['lr_rmse']:.4f}")
    
    # Random Forest
    with col2:
        st.subheader("Random Forest")
        st.metric("R² Score", f"{models_data['rf_r2']:.4f}")
        st.metric("RMSE", f"{models_data['rf_rmse']:.4f}")
    
    # Best Model
    with col3:
        st.subheader("🏆 Best Model")
        st.metric("Model", models_data['model_name'])
        st.metric("R² Score", f"{models_data['best_r2']:.4f}")
        st.metric("RMSE", f"{models_data['best_rmse']:.4f}")
    
    st.divider()
    
    # Performance visualization
    models_comparison = pd.DataFrame({
        'Model': ['Linear Regression', 'Random Forest', models_data['model_name']],
        'R² Score': [models_data['lr_r2'], models_data['rf_r2'], models_data['best_r2']]
    })
    
    fig = px.bar(models_comparison, x='Model', y='R² Score',
                title="Model R² Score Comparison",
                color='R² Score',
                color_continuous_scale='Greens',
                text='R² Score')
    fig.update_traces(texttemplate='%{text:.4f}', textposition='outside')
    st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    main()
