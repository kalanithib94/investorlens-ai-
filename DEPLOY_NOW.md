# 🚀 Deploy InvestorLens AI - Step by Step

## ✅ Current Status: Code committed locally
**Next: Push to GitHub and deploy!**

---

## Step 1: Push to GitHub (5 minutes)

### 1.1 Create GitHub Repository
1. Go to https://github.com/new
2. Repository name: **`investorlens-ai`** (or your choice)
3. Description: **"AI-powered portfolio intelligence platform for VC firms"**
4. Keep it **Public** (to show in interviews)
5. **DO NOT** initialize with README, gitignore, or license (we already have these)
6. Click "Create repository"

### 1.2 Push Your Code
After creating the repo, run these commands in PowerShell:

```powershell
cd "C:\Users\Kala\Desktop\Mine\Resume\Saphhire\Project"

# Add your GitHub repository (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/investorlens-ai.git

# Rename branch to main
git branch -M main

# Push to GitHub
git push -u origin main
```

**✅ Checkpoint:** Visit your GitHub repo - you should see all 47 files!

---

## Step 2: Deploy Backend to Railway (10 minutes)

### 2.1 Sign Up for Railway
1. Go to https://railway.app
2. Click "Login" → Sign in with GitHub
3. Authorize Railway to access your repositories

### 2.2 Create New Project
1. Click "New Project"
2. Select "Deploy from GitHub repo"
3. Choose your **`investorlens-ai`** repository
4. Click "Deploy Now"

### 2.3 Add PostgreSQL Database
1. In your Railway project dashboard, click **"+ New"**
2. Select **"Database"** → **"PostgreSQL"**
3. Wait 1-2 minutes for provisioning
4. ✅ Railway automatically sets `DATABASE_URL` environment variable

### 2.4 Configure Backend Service
1. Click on your backend service (should auto-detect)
2. Go to **"Settings"** tab
3. Under **"Root Directory"**, enter: **`backend`**
4. Click **"Save"**

### 2.5 Set Environment Variables
1. In backend service, go to **"Variables"** tab
2. Click **"+ New Variable"** and add:

```
SECRET_KEY = your-secret-key-here
OPENAI_API_KEY = sk-your-openai-key (optional but recommended)
NEWS_API_KEY = your-newsapi-key (optional)
CORS_ORIGINS = *
```

**Generate SECRET_KEY:**
```python
# Run in Python
import secrets
print(secrets.token_urlsafe(32))
```

**Get OPENAI_API_KEY (optional but recommended):**
- Go to https://platform.openai.com/api-keys
- Create new secret key
- Copy and paste

3. Click **"Deploy"** to restart with new variables

### 2.6 Get Your Backend URL
1. Go to **"Settings"** → **"Networking"**
2. Under **"Public Networking"**, click **"Generate Domain"**
3. Copy your Railway URL (e.g., `investorlens-production.up.railway.app`)

### 2.7 Initialize Database
1. In Railway, go to your backend service
2. Click **"Deployments"** → Select latest deployment
3. Click **"View Logs"**
4. Wait for deployment to complete
5. Open terminal tab (if available) or use local terminal:

```bash
# Set DATABASE_URL to your Railway PostgreSQL URL
# You can find it in Railway: PostgreSQL service → Connect → Copy connection string

# Then run:
python backend/scripts/init_db.py
# Type 'y' to create sample data
```

**✅ Checkpoint:** Visit `https://your-railway-url.up.railway.app/health`
Should return: `{"status":"healthy"}`

**✅ Test API Docs:** Visit `https://your-railway-url.up.railway.app/docs`
Should show Swagger UI with all 25+ endpoints!

---

## Step 3: Deploy Frontend to Vercel (5 minutes)

### 3.1 Sign Up for Vercel
1. Go to https://vercel.com
2. Click "Sign Up" → Continue with GitHub
3. Authorize Vercel

### 3.2 Import Project
1. Click **"Add New..."** → **"Project"**
2. Find and **"Import"** your **`investorlens-ai`** repository

### 3.3 Configure Build Settings
1. **Framework Preset:** Vite (should auto-detect)
2. **Root Directory:** Click **"Edit"** → Enter **`frontend`**
3. **Build Command:** `npm run build` (default)
4. **Output Directory:** `dist` (default)

### 3.4 Set Environment Variable
1. Click **"Environment Variables"**
2. Add variable:
   - **Key:** `VITE_API_URL`
   - **Value:** `https://your-railway-backend-url.up.railway.app`
   - (Use the Railway URL from Step 2.6)
3. Click **"Add"**

### 3.5 Deploy
1. Click **"Deploy"**
2. Wait 2-3 minutes for build
3. ✅ You'll get a URL like `investorlens-ai.vercel.app`

**✅ Checkpoint:** Visit your Vercel URL
You should see the InvestorLens AI dashboard!

### 3.6 Update Backend CORS (Important!)
1. Go back to **Railway** → Backend service → **Variables**
2. Edit `CORS_ORIGINS`:
   - Change from `*` to your Vercel URL:
   - `https://your-app.vercel.app`
3. Save and redeploy

---

## Step 4: Verify Everything Works (2 minutes)

### Backend Checks
- ✅ Health: `https://your-railway-url.up.railway.app/health`
- ✅ API Docs: `https://your-railway-url.up.railway.app/docs`
- ✅ Get Companies: `https://your-railway-url.up.railway.app/api/companies`

### Frontend Checks
- ✅ Homepage loads: `https://your-vercel-url.vercel.app`
- ✅ Sample companies displayed
- ✅ Alert panel shows
- ✅ No errors in browser console (F12)

### Test Full Integration
1. Open frontend in browser
2. Open browser DevTools (F12) → Network tab
3. Refresh page
4. Look for successful API calls to your Railway backend

---

## 🎉 Success! Your App is Live!

Save these URLs:
- **Frontend:** `https://your-app.vercel.app`
- **Backend API:** `https://your-backend.up.railway.app`
- **API Docs:** `https://your-backend.up.railway.app/docs`
- **GitHub:** `https://github.com/YOUR_USERNAME/investorlens-ai`

---

## 📝 Update Your Main README

Add these URLs to your main `README.md` at the workspace root:

```markdown
# InvestorLens AI - Live Demo

🌐 **Live Application:** https://your-app.vercel.app
📚 **API Documentation:** https://your-backend.up.railway.app/docs
💻 **GitHub Repository:** https://github.com/YOUR_USERNAME/investorlens-ai

Built for KTP Associate position at Sapphire Capital Partners
```

---

## 🎯 For Your Interview

### Demo Script
1. **Show Frontend:** "This is InvestorLens AI, live on Vercel's edge network"
2. **Click Company Card:** "Each company has real-time risk scoring"
3. **Show Alerts:** "AI-powered alerts with severity levels"
4. **Open API Docs:** "25+ RESTful endpoints with auto-generated documentation"
5. **Show GitHub:** "Full CI/CD pipeline with automated testing"

### Key Stats to Mention
- **47 files, 4,931 lines of code**
- **25+ API endpoints**
- **3 database models**
- **Unit and integration tests**
- **Deployed on Railway + Vercel**
- **Built in modern tech stack**

---

## 🆘 Troubleshooting

### Backend won't start
- Check Railway logs: Backend service → Deployments → View Logs
- Verify `DATABASE_URL` is set (should be automatic)
- Ensure `backend` is set as root directory

### Frontend shows "Backend connection unavailable"
- Verify `VITE_API_URL` in Vercel
- Check backend health endpoint directly
- Verify CORS_ORIGINS includes your Vercel URL

### No sample data showing
- Need to run `init_db.py` script
- Can use Railway CLI or local connection
- Or manually add companies via API docs `/docs`

### Database connection error
- PostgreSQL must be in same Railway project
- `DATABASE_URL` auto-set by Railway
- Check Railway logs for detailed error

---

## ✅ Deployment Checklist

Backend (Railway):
- [ ] GitHub repo pushed
- [ ] Railway project created
- [ ] PostgreSQL database added
- [ ] Root directory set to `backend`
- [ ] Environment variables configured
- [ ] Backend deployed successfully
- [ ] Health endpoint working
- [ ] API docs accessible
- [ ] Database initialized

Frontend (Vercel):
- [ ] Vercel project created
- [ ] Root directory set to `frontend`
- [ ] `VITE_API_URL` configured
- [ ] Frontend deployed successfully
- [ ] Dashboard loads correctly
- [ ] API calls working
- [ ] Sample companies showing

Final Steps:
- [ ] Update README with live URLs
- [ ] Test full application flow
- [ ] Bookmark all important URLs
- [ ] Practice interview demo

---

**🎊 Congratulations! You have a live, production application to showcase in your interview!**

---

## 📞 Need Help?

If you get stuck:
1. Check Railway/Vercel logs for errors
2. Review `DEPLOYMENT_GUIDE.md` for detailed troubleshooting
3. Verify all environment variables are set correctly
4. Check that root directories are correctly configured

**Your InvestorLens AI platform is ready to impress Sapphire Capital Partners! 🚀**

