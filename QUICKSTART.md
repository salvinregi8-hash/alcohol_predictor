# Quick Start Guide 🚀

## Running Locally (5 minutes)

### Step 1: Install Python Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Run the App
```bash
streamlit run app.py
```

### Step 3: Open in Browser
- Automatically opens at: `http://localhost:8501`
- Or manually go to that address

### Step 4: Explore!
- 📊 Dashboard - View data infographics
- 🔮 Prediction - Make predictions
- 📈 Performance - Check model metrics

---

## Deploying to Cloud (10 minutes)

### Option A: Streamlit Cloud (Easiest) ⭐

1. **Push to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Beer app"
   git remote add origin https://github.com/YOUR-USERNAME/beer-servings.git
   git push -u origin main
   ```

2. **Deploy**
   - Go to https://share.streamlit.io
   - Click "New app"
   - Select your GitHub repo
   - Click Deploy!

3. **Share URL**
   ```
   https://your-app-name.streamlit.app
   ```

### Option B: PythonAnywhere

1. Create account at pythonanywhere.com
2. Upload files
3. Create web app
4. Configure Python environment
5. Visit: `https://yourname.pythonanywhere.com`

---

## Project Structure

```
streamlit_beer_app/
├── app.py                    # Main app
├── requirements.txt          # Dependencies
├── .streamlit/config.toml    # Settings
├── data/beer-servings.csv    # Dataset
├── README.md                 # Full docs
├── DEPLOYMENT_GUIDE.md       # Detailed steps
├── GITHUB_SETUP.md          # GitHub instructions
└── .gitignore               # Git ignore rules
```

---

## What the App Does

✨ **3 Pages**:

1. **📊 Dashboard**
   - Shows data statistics
   - Interactive charts
   - Beer/spirit/wine trends by continent

2. **🔮 Prediction**
   - Input beer, spirit, wine servings
   - Select country and continent
   - Get instant predictions
   - Compare with real data

3. **📈 Performance**
   - Model comparison
   - R² scores and RMSE
   - Best model metrics

---

## Features

✅ Machine Learning Models:
- Linear Regression
- Random Forest (tuned)
- Automatic model selection

✅ Beautiful UI:
- Plotly interactive charts
- Responsive design
- Professional styling

✅ Data-Driven:
- 140+ countries
- 6 continents
- Real-world data

---

## Technology Stack

- **Streamlit**: Web framework
- **Pandas**: Data handling
- **Scikit-learn**: ML models
- **Plotly**: Interactive visualizations

---

## Common Commands

```bash
# Run locally
streamlit run app.py

# Run on specific port
streamlit run app.py --server.port 8502

# Run in headless mode
streamlit run app.py --headless

# Clear cache
streamlit cache clear

# View help
streamlit --help
```

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Module not found | `pip install -r requirements.txt` |
| Port in use | `streamlit run app.py --server.port 8502` |
| Data not loading | Check `data/beer-servings.csv` exists |
| Slow app | Uses caching, should be fast |

---

## Need Help?

📚 **Documentation**:
- Streamlit: https://docs.streamlit.io
- Scikit-learn: https://scikit-learn.org
- Pandas: https://pandas.pydata.org

---

**You're ready to go! Happy predicting! 🍺**

*For detailed deployment instructions, see DEPLOYMENT_GUIDE.md*
