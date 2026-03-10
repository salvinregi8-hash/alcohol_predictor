# GitHub Repository Setup Guide

## Quick Start

### 1. Create a new GitHub repository
   - Go to https://github.com/new
   - Name: `beer-servings-prediction`
   - Description: "Beer Servings & Alcohol Consumption Prediction Web App"
   - Make it Public
   - Don't initialize with README (we have one)
   - Click "Create repository"

### 2. Initialize git and push code
   ```bash
   cd streamlit_beer_app
   git init
   git config user.name "Your Name"
   git config user.email "your.email@example.com"
   git add .
   git commit -m "Initial commit: Streamlit beer prediction app"
   git branch -M main
   git remote add origin https://github.com/YOUR-USERNAME/beer-servings-prediction.git
   git push -u origin main
   ```

### 3. Add .gitignore
   Create `.gitignore` file with:
   ```
   __pycache__/
   *.py[cod]
   *$py.class
   .streamlit/secrets.toml
   .env
   venv/
   env/
   .vscode/
   .idea/
   .DS_Store
   ```

### 4. Streamlit Cloud Deployment

   **Step 1: Link GitHub to Streamlit**
   - Go to https://share.streamlit.io
   - Click "New app"
   - Choose "GitHub" as source
   - Authorize Streamlit to access your GitHub account

   **Step 2: Deploy**
   - Select repository: `YOUR-USERNAME/beer-servings-prediction`
   - Branch: `main`
   - Main file path: `app.py`
   - Click "Deploy"

   **Step 3: Share**
   - Your app URL: `https://beer-servings-prediction.streamlit.app`
   - Copy and share the public URL

### 5. Repository Contents Checklist

   ✅ app.py - Main application
   ✅ requirements.txt - Dependencies
   ✅ .streamlit/config.toml - Configuration
   ✅ data/beer-servings.csv - Dataset
   ✅ README.md - Documentation
   ✅ .gitignore - Git ignore file

### Environment Variables (if needed)

If you need to add secrets for production:

1. Create `.streamlit/secrets.toml` in your local repo (don't push to GitHub):
   ```toml
   api_key = "your-secret-key"
   ```

2. On Streamlit Cloud:
   - Go to your app settings
   - Click "Secrets"
   - Paste the contents of `.streamlit/secrets.toml`

### Updating the App

After making changes locally:

```bash
git add .
git commit -m "Description of changes"
git push
```

Streamlit Cloud will automatically redeploy!

### Troubleshooting Deployment

**App won't start**
- Check requirements.txt for version conflicts
- Ensure all imports in app.py are listed in requirements
- Check logs in Streamlit Cloud dashboard

**Data not loading**
- Verify `data/beer-servings.csv` is committed to git
- Check file paths in app.py (use relative paths)

**Memory issues**
- Consider smaller dataset or optimize model training
- Use caching decorators (@st.cache_resource, @st.cache_data)

### Additional Resources

- Streamlit Documentation: https://docs.streamlit.io
- Streamlit Cloud Docs: https://docs.streamlit.io/deploy
- GitHub Docs: https://docs.github.com

---

Once deployed, share your public URL:
```
https://beer-servings-prediction.streamlit.app
```
