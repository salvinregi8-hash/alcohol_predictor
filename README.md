# 🍺 Beer Servings Prediction - Basic Version

A simple Streamlit app to predict alcohol consumption based on beverage servings.

## Quick Start

```bash
# 1. Extract the ZIP
unzip streamlit_beer_app_basic.zip
cd streamlit_beer_basic

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
streamlit run app.py
```

That's it! The app opens at http://localhost:8501

## Features

### 📊 Dashboard Page
- Statistics overview
- Data grouped by continent
- Sample data table

### 🔮 Prediction Page
- Input beer, spirit, and wine servings
- Select country and continent
- Get instant predictions
- Compare with actual values

### 📈 Performance Page
- Linear Regression metrics
- Random Forest metrics
- Best model comparison

## Requirements

- Python 3.7+
- pandas
- numpy
- scikit-learn
- streamlit

## Deploy to Streamlit Cloud

1. Push to GitHub:
```bash
git init
git add .
git commit -m "Basic beer app"
git remote add origin https://github.com/YOUR-USERNAME/beer-app.git
git push -u origin main
```

2. Go to https://share.streamlit.io
3. Click "New app"
4. Select your GitHub repo
5. Click Deploy!

## Notes

- This is a minimal version for compatibility
- Uses only essential libraries
- No complex visualizations (for stability)
- Works on all Python versions
- Streamlit Cloud friendly

## Dataset

140+ countries with alcohol consumption data across 6 continents.
