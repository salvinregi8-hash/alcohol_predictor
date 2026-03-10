# Beer Servings Prediction Web App 🍺

A Streamlit web application for predicting total alcohol consumption based on beer, spirit, and wine servings across different countries and continents.

## Features

✨ **Interactive Dashboard**
- Data infographics and visualizations
- Statistical overview of alcohol consumption
- Interactive charts using Plotly

🔮 **Prediction Interface**
- Input numerical values for beer, spirit, and wine servings
- Dropdown menus for country and continent selection
- Real-time predictions using trained ML models
- Comparison with actual data

📈 **Model Performance**
- Comparison of Linear Regression and Random Forest models
- R² score and RMSE metrics
- Hyperparameter tuning results
- Best model selection

## Project Structure

```
streamlit_beer_app/
├── app.py                      # Main Streamlit application
├── requirements.txt            # Python dependencies
├── .streamlit/
│   └── config.toml            # Streamlit configuration
├── data/
│   └── beer-servings.csv      # Beer servings dataset
└── README.md                  # This file
```

## Installation & Local Development

### Prerequisites
- Python 3.8+
- pip

### Steps

1. **Clone or extract the project**
   ```bash
   cd streamlit_beer_app
   ```

2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app locally**
   ```bash
   streamlit run app.py
   ```

5. **Access the app**
   - Open your browser and go to `http://localhost:8501`

## Deployment to Streamlit Cloud

### Prerequisites
- GitHub account
- GitHub repository with this code
- Streamlit account (free at https://streamlit.io)

### Steps

1. **Push code to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/your-username/your-repo.git
   git push -u origin main
   ```

2. **Deploy on Streamlit Cloud**
   - Go to https://share.streamlit.io
   - Click "New app"
   - Select your GitHub repository
   - Select the branch and file (app.py)
   - Click "Deploy"

3. **Share the public URL**
   - Your app will be deployed at: `https://your-app-name.streamlit.app`

### Alternative: Deploy to PythonAnywhere

1. **Create account at pythonanywhere.com**

2. **Upload files to web app**

3. **Configure WSGI**

4. **Set up virtual environment and install dependencies**

5. **Reload the web app**

## Dataset

The app uses the Beer Servings dataset containing:
- **Country**: Country name
- **Beer_servings**: Average beer servings per capita per year
- **Spirit_servings**: Average spirit servings per capita per year
- **Wine_servings**: Average wine servings per capita per year
- **Continent**: Continent where country is located
- **total_litres_of_pure_alcohol**: Total pure alcohol consumption in litres

## Machine Learning Models

### Models Implemented
1. **Linear Regression** - Baseline model with feature scaling
2. **Random Forest** - Ensemble method with hyperparameter tuning

### Best Model Selection
The app automatically selects the best model based on:
- R² Score (higher is better)
- RMSE (lower is better)

### Hyperparameter Tuning
The Random Forest model is tuned with:
- n_estimators: 100-150
- max_depth: 10-12
- min_samples_split: 2-5
- min_samples_leaf: 2

## Usage Guide

### 1. Dashboard Page
- View overall statistics
- Explore data visualizations
- Understand patterns in alcohol consumption across continents

### 2. Prediction Page
- Input beverage servings (beer, spirit, wine)
- Select country and continent
- Get instant predictions
- Compare with actual values

### 3. Model Performance Page
- Compare model metrics
- View R² scores and RMSE values
- Understand model selection rationale

## Technologies Used

- **Streamlit**: Web framework
- **Pandas**: Data manipulation
- **NumPy**: Numerical computing
- **Scikit-learn**: Machine learning
- **Plotly**: Interactive visualizations

## Requirements

See `requirements.txt` for exact versions:
- streamlit==1.28.1
- pandas==2.0.3
- numpy==1.24.3
- scikit-learn==1.3.0
- plotly==5.17.0

## Notes

- The app handles categorical encoding automatically
- Features are scaled using StandardScaler for better model performance
- Data is cached for faster loading
- Models are trained once and cached in memory

## Troubleshooting

### Port already in use
```bash
streamlit run app.py --logger.level=debug --server.port 8502
```

### Module not found errors
```bash
pip install --upgrade -r requirements.txt
```

### Data file not found
The app includes fallback logic to create sample data if the CSV is missing.

## License

This project is for educational purposes as part of the MLAI course.

## Contact & Support

For issues or questions about the deployment, please refer to:
- Streamlit Documentation: https://docs.streamlit.io
- Scikit-learn Documentation: https://scikit-learn.org/stable/
- GitHub Issues: [Your repository]

---

Happy predicting! 🍺📊
