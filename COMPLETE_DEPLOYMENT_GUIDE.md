# 🚀 Complete Deployment Guide - InvestorLens AI

This guide will deploy your complete InvestorLens AI platform:
- ✅ **Git**: Already pushed to GitHub
- 🚂 **Backend**: Railway
- ⚡ **Frontend**: Vercel

---

## ✅ Git Deployment - COMPLETE! 

Your code has been successfully pushed to GitHub:
- **Repository**: https://github.com/kalanithib94/investorlens-ai-.git
- **Branch**: main
- **Last Commit**: "Frontend ready for Vercel deployment"
- **Files Updated**: 10 files (7,780 additions)

---

## 🚂 Railway Deployment (Backend)

Your backend is already configured for Railway! Here's how to deploy:

### Option 1: Via Railway Dashboard (Recommended)

1. **Go to Railway**: [railway.app](https://railway.app)

2. **Login/Sign Up**: Use GitHub for easy integration

3. **Create New Project**:
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose: `kalanithib94/investorlens-ai-`
   - Railway will auto-detect your Python app

4. **Configure Backend Service**:
   - Root Directory: `backend`
   - Start Command: `bash start.sh` (already in railway.json)
   - Click "Deploy"

5. **Add Environment Variables**:
   
   Go to your backend service → Variables → Add these:

   ```bash
   # Database (Railway provides PostgreSQL)
   DATABASE_URL=<auto-provided-by-railway-postgres>
   
   # Redis (optional, Railway provides)
   REDIS_URL=<auto-provided-by-railway-redis>
   
   # Security
   SECRET_KEY=<generate-secure-random-string>
   
   # CORS (IMPORTANT - Add after Vercel deployment)
   CORS_ORIGINS=["http://localhost:3000","http://localhost:5173","https://your-vercel-app.vercel.app","https://your-vercel-app-*.vercel.app"]
   
   # AI API Keys (Optional but recommended)
   OPENAI_API_KEY=<your-key>
   ANTHROPIC_API_KEY=<your-key>
   
   # External APIs (Optional)
   NEWS_API_KEY=<your-key>
   ```

6. **Add PostgreSQL Database**:
   - In your project, click "New"
   - Select "Database" → "PostgreSQL"
   - Railway auto-links DATABASE_URL to your backend

7. **Add Redis (Optional)**:
   - Click "New" → "Database" → "Redis"
   - Railway auto-links REDIS_URL

8. **Deploy**:
   - Railway automatically deploys
   - Wait 2-3 minutes
   - Check logs for any errors

9. **Get Your Backend URL**:
   - Go to Settings → Generate Domain
   - Copy the URL (e.g., `https://your-app.up.railway.app`)
   - **Save this URL** - you'll need it for Vercel!

### Option 2: Via Railway CLI

```bash
# Install Railway CLI
npm i -g @railway/cli

# Login
railway login

# Initialize project
railway init

# Link to backend
cd backend

# Deploy
railway up

# Add variables
railway variables set DATABASE_URL=<url>
railway variables set SECRET_KEY=<key>
# ... add other variables

# Check status
railway status

# View logs
railway logs
```

---

## ⚡ Vercel Deployment (Frontend)

### Option 1: Automated Script (Easiest)

I've created a deployment script for you! Simply run:

```powershell
# From project root
.\deploy-vercel.ps1
```

This script will:
- ✅ Check Vercel CLI installation
- ✅ Login to Vercel (opens browser)
- ✅ Deploy to production
- ✅ Show next steps

### Option 2: Manual Deployment

```powershell
# Navigate to frontend
cd frontend

# Login to Vercel
vercel login
# → Select "Continue with GitHub"
# → Complete authentication in browser

# Deploy to production
vercel --prod

# Follow the prompts:
# - Set up and deploy? Y
# - Which scope? (Select your account)
# - Link to existing project? N (first time)
# - Project name? investorlens-frontend
# - Directory? ./ (press Enter)
```

### Option 3: Via GitHub Integration (Best for Teams)

1. **Go to Vercel**: [vercel.com/new](https://vercel.com/new)

2. **Import Repository**:
   - Click "Add New..." → "Project"
   - Import: `kalanithib94/investorlens-ai-`
   - Click "Import"

3. **Configure Project**:
   - Framework: **Vite** ✅
   - Root Directory: **`frontend`** ⚠️ **CRITICAL!**
   - Build Command: `npm run build` (auto)
   - Output Directory: `dist` (auto)

4. **Click Deploy**: Wait 2-3 minutes

---

## 🔧 Post-Deployment Configuration

### Step 1: Add Environment Variable to Vercel

1. Go to [Vercel Dashboard](https://vercel.com/dashboard)
2. Select your project (investorlens-frontend)
3. Go to: Settings → Environment Variables
4. Add variable:
   - **Name**: `VITE_API_URL`
   - **Value**: Your Railway backend URL (e.g., `https://your-app.up.railway.app`)
   - **Environments**: Check all (Production, Preview, Development)
5. Click "Save"
6. **Redeploy**: Go to Deployments → Latest → "..." → Redeploy

### Step 2: Update Backend CORS

1. Go to Railway Dashboard
2. Select your backend service
3. Go to: Variables
4. Update `CORS_ORIGINS` with your Vercel URL:

```json
["http://localhost:3000","http://localhost:5173","https://your-vercel-app.vercel.app","https://your-vercel-app-*.vercel.app"]
```

5. Save (Railway will auto-redeploy)

### Step 3: Test Complete Integration

1. **Visit your Vercel URL**
2. **Open Browser DevTools** (F12)
3. **Check Console**: No CORS errors
4. **Check Network Tab**: API calls working
5. **Test Features**:
   - Dashboard loads
   - Data displays
   - No errors

---

## 📊 Deployment Summary

Once complete, you'll have:

| Component | Platform | URL | Status |
|-----------|----------|-----|--------|
| **Code** | GitHub | https://github.com/kalanithib94/investorlens-ai-.git | ✅ Deployed |
| **Backend** | Railway | `https://your-app.up.railway.app` | ⏳ Pending |
| **Frontend** | Vercel | `https://your-app.vercel.app` | ⏳ Pending |
| **Database** | Railway | PostgreSQL (auto-linked) | ⏳ Pending |

---

## 🎯 Quick Deployment Checklist

### Git ✅
- [x] All changes committed
- [x] Pushed to GitHub
- [x] Repository: kalanithib94/investorlens-ai-

### Railway (Backend) ⏳
- [ ] Project created on Railway
- [ ] Backend deployed from GitHub
- [ ] PostgreSQL database added
- [ ] Environment variables configured
- [ ] Backend URL generated
- [ ] Health check passing (/health endpoint)

### Vercel (Frontend) ⏳
- [ ] Vercel CLI login completed
- [ ] Frontend deployed to production
- [ ] VITE_API_URL environment variable added
- [ ] Project redeployed after env var
- [ ] Frontend loads without errors

### Integration ⏳
- [ ] Backend CORS updated with Vercel URL
- [ ] Frontend can connect to backend
- [ ] No CORS errors in browser console
- [ ] API calls working
- [ ] Dashboard displays data

---

## 🐛 Troubleshooting

### Backend Issues

**Issue**: Railway build fails
```bash
Solution: 
- Check backend/requirements.txt
- Ensure Python version in runtime.txt
- Check Railway build logs
```

**Issue**: Database connection fails
```bash
Solution:
- Verify DATABASE_URL in Railway variables
- Check PostgreSQL service is running
- Test connection: railway run python -c "from app.core.database import init_db; init_db()"
```

**Issue**: Health check fails
```bash
Solution:
- Test locally: curl http://localhost:8000/health
- Check start.sh is executable
- Review Railway logs
```

### Frontend Issues

**Issue**: Vercel login fails
```bash
Solution:
- Clear browser cache
- Try different browser
- Use: vercel login --github
```

**Issue**: Build fails on Vercel
```bash
Solution:
- Verify Root Directory = "frontend"
- Test locally: cd frontend && npm run build
- Check Vercel build logs
```

**Issue**: CORS errors
```bash
Solution:
- Add Vercel domain to backend CORS_ORIGINS
- Redeploy backend after CORS update
- Clear browser cache
```

**Issue**: API calls fail
```bash
Solution:
- Verify VITE_API_URL in Vercel
- Redeploy after adding env var
- Check backend is accessible: curl <railway-url>/health
```

---

## 🔐 Security Checklist

Before going live:

- [ ] SECRET_KEY is strong random string (not default)
- [ ] Database passwords are secure
- [ ] API keys stored in environment variables (not code)
- [ ] CORS only allows your domains
- [ ] HTTPS enabled (automatic on Vercel/Railway)
- [ ] .env files in .gitignore
- [ ] No sensitive data committed to Git

---

## 📞 Support Resources

- **Frontend Guide**: `frontend/VERCEL_DEPLOYMENT.md`
- **Quick Start**: `VERCEL_READY.md`
- **Checklist**: `frontend/DEPLOYMENT_CHECKLIST.md`
- **Project Docs**: `frontend/README.md`

### Platform Documentation

- **Railway**: [docs.railway.app](https://docs.railway.app)
- **Vercel**: [vercel.com/docs](https://vercel.com/docs)
- **GitHub**: Your repo at https://github.com/kalanithib94/investorlens-ai-

---

## 🎉 Success Metrics

Your deployment is successful when:

✅ Backend health check returns 200 OK  
✅ Frontend loads without console errors  
✅ Dashboard displays (even if empty)  
✅ API calls succeed (check Network tab)  
✅ No CORS errors  
✅ All three services (GitHub, Railway, Vercel) show green status  

---

## 🚀 Next Steps After Deployment

1. **Test thoroughly** on different devices
2. **Add monitoring** (Vercel Analytics, Railway metrics)
3. **Set up alerts** for downtime
4. **Document your URLs** for the team
5. **Enable auto-deployments** (already enabled with GitHub integration)
6. **Add custom domain** (optional)
7. **Set up CI/CD** for automated testing

---

## 💡 Pro Tips

1. **Preview Deployments**: Every PR gets unique preview URL on Vercel
2. **Database Backups**: Enable on Railway (Settings → Backups)
3. **Monitoring**: Use Railway's built-in metrics
4. **Logs**: Check Railway/Vercel logs for issues
5. **Rollbacks**: Easy rollback in Vercel (Deployments → Select → Promote)

---

**You've got this! 🎉**

Follow the steps above, and your InvestorLens AI platform will be live in 15-20 minutes!

Need help? Check the detailed guides in the `frontend/` directory.

