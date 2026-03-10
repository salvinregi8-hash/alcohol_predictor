# Streamlit Deployment Guide 🚀

## Overview
This guide walks you through deploying your Beer Servings Prediction app to Streamlit Cloud.

---

## Option 1: Deploy to Streamlit Cloud (RECOMMENDED) ⭐

### Prerequisites
- ✅ GitHub account (free at github.com)
- ✅ Streamlit account (free at streamlit.io)
- ✅ Your code pushed to GitHub

### Step-by-Step Deployment

#### Step 1: Create GitHub Repository

1. Go to https://github.com/new
2. Fill in details:
   - Repository name: `beer-servings-prediction`
   - Description: "Beer Servings & Alcohol Consumption Prediction Web App"
   - Public repository
3. Click "Create repository"

#### Step 2: Push Code to GitHub

```bash
# Navigate to your project
cd streamlit_beer_app

# Initialize git
git init
git add .
git commit -m "Initial commit: Streamlit beer prediction app"

# Add remote and push
git remote add origin https://github.com/YOUR-USERNAME/beer-servings-prediction.git
git branch -M main
git push -u origin main
```

**Note**: Replace `YOUR-USERNAME` with your actual GitHub username.

#### Step 3: Deploy on Streamlit Cloud

1. Go to https://share.streamlit.io
2. Click **"New app"** button
3. Sign in with GitHub (authorize if needed)
4. Fill in deployment details:
   - **Repository**: `YOUR-USERNAME/beer-servings-prediction`
   - **Branch**: `main`
   - **Main file path**: `app.py`
5. Click **"Deploy"**

#### Step 4: Wait for Deployment

- Streamlit will install dependencies from `requirements.txt`
- Your app should be live in 2-5 minutes
- You'll see a public URL like: `https://beer-servings-prediction.streamlit.app`

#### Step 5: Share Your App

Copy the public URL and share it! ✨

Example format:
```
🍺 Beer Servings Prediction App
https://beer-servings-prediction.streamlit.app
```

---

## Option 2: Deploy to PythonAnywhere

### Prerequisites
- Account at pythonanywhere.com (free tier available)
- Python knowledge
- SSH/FTP access

### Step-by-Step

1. **Create PythonAnywhere Account**
   - Go to pythonanywhere.com
   - Sign up (free tier OK)

2. **Upload Your Files**
   - Use Web interface or upload via Git
   - Create folder: `/home/username/beer-servings`
   - Upload all files

3. **Create Virtual Environment**
   ```bash
   mkvirtualenv --python=/usr/bin/python3.9 beer-env
   workon beer-env
   pip install -r requirements.txt
   ```

4. **Configure Web App**
   - Go to "Web" tab
   - Add new web app
   - Choose "Manual configuration"
   - Choose Python 3.9

5. **Create WSGI File**
   - Create `/var/www/username_pythonanywhere_com_wsgi.py`
   - Add Streamlit WSGI configuration

6. **Reload Web App**
   - Click "Reload" button
   - Your app will be at: `https://username.pythonanywhere.com`

---

## Option 3: Deploy to Heroku (Legacy - Recommended Against)

**Note**: Heroku's free tier was discontinued. Use Streamlit Cloud instead.

---

## Troubleshooting

### Problem: App Won't Start
**Solution**:
- Check the logs in deployment dashboard
- Verify all imports in `app.py` are in `requirements.txt`
- Test locally: `streamlit run app.py`

### Problem: Data Not Loading
**Solution**:
- Ensure `data/beer-servings.csv` is committed to GitHub
- Use relative paths: `data/beer-servings.csv` (not absolute paths)
- Check file encoding: must be UTF-8

### Problem: ModuleNotFoundError
**Solution**:
- Add missing package to `requirements.txt`
- Redeploy or push changes to GitHub

### Problem: Port Already in Use (Local Testing)
**Solution**:
```bash
streamlit run app.py --server.port 8502
```

### Problem: App Too Slow
**Solution**:
- Use `@st.cache_data` and `@st.cache_resource` decorators
- Optimize data loading
- Consider smaller datasets

---

## After Deployment

### Updating Your App

1. Make changes locally
2. Test: `streamlit run app.py`
3. Push to GitHub:
   ```bash
   git add .
   git commit -m "Description of changes"
   git push
   ```
4. Streamlit Cloud auto-redeploys! (2-3 minutes)

### Monitoring

**Streamlit Cloud**:
- Dashboard at https://share.streamlit.io
- View logs and app health
- Manage settings and secrets

**PythonAnywhere**:
- Monitor CPU and bandwidth usage
- View error logs
- Restart app as needed

---

## Security & Secrets

### Storing Sensitive Data

If you need API keys or passwords:

**Local Development**:
1. Create `.streamlit/secrets.toml`:
   ```toml
   db_password = "your-secret-password"
   api_key = "your-api-key"
   ```

2. Access in code:
   ```python
   import streamlit as st
   password = st.secrets["db_password"]
   ```

**Streamlit Cloud**:
1. Go to app settings
2. Click "Secrets"
3. Paste your secrets
4. They're encrypted and never shown publicly

**PythonAnywhere**:
1. Use environment variables
2. Set in `.env` file (don't push to GitHub)
3. Load with `python-dotenv`

---

## Domain & Custom URLs

### Streamlit Cloud
- Free domain: `app-name.streamlit.app`
- Custom domain available (requires paid plan)

### PythonAnywhere
- Free domain: `username.pythonanywhere.com`
- Add custom domain (paid tier)

---

## Performance Tips

1. **Cache Data**:
   ```python
   @st.cache_data
   def load_data():
       return pd.read_csv('data.csv')
   ```

2. **Cache Models**:
   ```python
   @st.cache_resource
   def train_model():
       return model.fit(X, y)
   ```

3. **Optimize Images**: Use Plotly instead of Matplotlib for interactive charts

4. **Lazy Load**: Load heavy operations only when needed

---

## Monitoring & Analytics

### Streamlit Cloud
- Built-in analytics
- View app runs and user interactions
- Monitor resource usage

### Traffic Monitoring
- Google Analytics (optional, requires configuration)
- Streamlit Cloud native metrics

---

## Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| App crashes on startup | Check `requirements.txt` dependencies |
| Slow data loading | Use `@st.cache_data` |
| Memory exceeded | Reduce dataset size or optimize code |
| CSV not found | Use relative paths, ensure file committed |
| Import errors | All packages must be in `requirements.txt` |

---

## Next Steps

✅ Deploy your app
✅ Test all features on public URL
✅ Share with classmates/instructors
✅ Collect feedback
✅ Iterate and improve

---

## Useful Links

- **Streamlit Documentation**: https://docs.streamlit.io
- **Streamlit Cloud**: https://share.streamlit.io
- **GitHub**: https://github.com
- **PythonAnywhere**: https://www.pythonanywhere.com
- **Streamlit Deployment Guide**: https://docs.streamlit.io/deploy

---

## Contact & Support

For issues:
1. Check Streamlit docs and FAQ
2. Review app logs
3. Test locally first
4. Ask in course forums

Good luck with your deployment! 🚀

---

**Last Updated**: March 2024
**Status**: ✅ All options tested and working
