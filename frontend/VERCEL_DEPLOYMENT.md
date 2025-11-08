# 🚀 Vercel Deployment Guide - InvestorLens AI Frontend

This guide walks you through deploying the InvestorLens AI frontend to Vercel.

## ✅ Pre-Deployment Checklist

- [ ] Backend deployed and running (e.g., on Railway)
- [ ] Backend URL available (e.g., `https://your-app.up.railway.app`)
- [ ] Backend CORS configured to allow Vercel domain
- [ ] Vercel account created (free tier works!)

## 📋 Deployment Options

### Option A: Deploy via Vercel CLI (Recommended for Quick Testing)

#### 1. Install Vercel CLI

```bash
npm install -g vercel
```

#### 2. Login to Vercel

```bash
vercel login
```

Follow the prompts to authenticate (via GitHub, GitLab, or email).

#### 3. Deploy

Navigate to the frontend directory:

```bash
cd frontend
```

Deploy to preview:

```bash
vercel
```

Follow the prompts:
- Set up and deploy? **Y**
- Which scope? Select your account
- Link to existing project? **N** (first time)
- What's your project's name? **investorlens-frontend** (or your choice)
- In which directory is your code located? **./** (press Enter)

#### 4. Deploy to Production

Once preview looks good:

```bash
vercel --prod
```

Your app will be live at `https://your-project.vercel.app`!

---

### Option B: Deploy via GitHub + Vercel Dashboard (Recommended for Production)

#### 1. Push to GitHub

If not already done:

```bash
# From project root
git init
git add .
git commit -m "Initial commit - InvestorLens AI"
git branch -M main
git remote add origin <your-github-repo-url>
git push -u origin main
```

#### 2. Import to Vercel

1. Go to [vercel.com](https://vercel.com)
2. Click **"Add New..."** → **"Project"**
3. Import your GitHub repository
4. Select the repository

#### 3. Configure Project Settings

**IMPORTANT:** Configure these settings:

- **Framework Preset:** Vite ✅
- **Root Directory:** `frontend` ⚠️ **CRITICAL!**
- **Build Command:** `npm run build` (auto-detected)
- **Output Directory:** `dist` (auto-detected)
- **Install Command:** `npm install` (auto-detected)

#### 4. Add Environment Variables

Click **"Environment Variables"** and add:

| Name | Value | Environment |
|------|-------|-------------|
| `VITE_API_URL` | `https://your-backend.railway.app` | Production, Preview, Development |

⚠️ **Replace with your actual backend URL!**

#### 5. Deploy

Click **"Deploy"** and wait 2-3 minutes.

Your app will be live at `https://your-project.vercel.app`!

---

## 🔧 Post-Deployment Configuration

### 1. Update Backend CORS

Your backend must allow requests from your Vercel domain.

#### For Railway Backend:

1. Go to Railway Dashboard → Your Backend Service → Variables
2. Update `CORS_ORIGINS` to include:

```json
["http://localhost:3000","http://localhost:5173","https://your-app.vercel.app","https://your-app-*.vercel.app"]
```

The `*` wildcard allows preview deployments (each branch/PR gets unique URL).

#### Manual Backend Update:

In `backend/app/core/config.py`, update:

```python
CORS_ORIGINS: List[str] = [
    "http://localhost:3000",
    "http://localhost:5173", 
    "https://your-app.vercel.app",
    "https://your-app-*.vercel.app"  # For preview deployments
]
```

### 2. Test Your Deployment

1. Visit your Vercel URL
2. Open Browser DevTools (F12) → Console
3. Check for any errors
4. Test API connectivity:
   - Dashboard should load
   - Companies should display (if backend has data)
   - No CORS errors in console

### 3. Configure Custom Domain (Optional)

1. Go to Vercel Dashboard → Your Project → Settings → Domains
2. Add your custom domain (e.g., `investorlens.yourdomain.com`)
3. Update DNS records as instructed
4. Add domain to backend CORS origins

---

## 🔄 Automatic Deployments

Once connected to GitHub:

- ✅ **Every push to `main`** triggers production deployment
- ✅ **Every PR** gets unique preview URL
- ✅ **Comments on PRs** with deployment link
- ✅ **Automatic rollbacks** if deployment fails

---

## 🐛 Troubleshooting

### Issue: API calls fail with CORS errors

**Symptoms:**
```
Access to XMLHttpRequest at 'https://backend.com/api' from origin 'https://app.vercel.app' 
has been blocked by CORS policy
```

**Solution:**
1. Check backend CORS configuration includes your Vercel domain
2. Redeploy backend after updating CORS
3. Clear browser cache and retry

### Issue: Environment variables not working

**Symptoms:**
- API calls go to wrong URL
- App tries to connect to localhost

**Solution:**
1. Verify `VITE_API_URL` is set in Vercel Dashboard → Settings → Environment Variables
2. Make sure it's set for all environments (Production, Preview, Development)
3. **Redeploy** - Vercel requires rebuild after env var changes:
   - Go to Deployments → Click "..." on latest → Redeploy

### Issue: 404 on page refresh

**Symptoms:**
- Direct URL navigation works
- Refreshing page shows 404

**Solution:**
- Already handled by `vercel.json` rewrites ✅
- If still occurring, verify `vercel.json` is in frontend directory

### Issue: Build fails

**Symptoms:**
- Deployment fails during build step
- Error in Vercel logs

**Solution:**
1. Check Vercel build logs for specific error
2. Test build locally:
   ```bash
   cd frontend
   npm install
   npm run build
   ```
3. Ensure all dependencies are in `package.json` (not just devDependencies)
4. Check that Root Directory is set to `frontend`

### Issue: Blank page after deployment

**Symptoms:**
- Build succeeds
- Page loads but shows blank screen
- Console shows errors

**Solution:**
1. Open DevTools console to see specific errors
2. Common causes:
   - Missing environment variables
   - API connection failures
   - Check Network tab for failed requests

---

## 📊 Monitoring & Analytics

### View Deployment Logs

```bash
vercel logs <deployment-url>
```

Or in Dashboard:
1. Go to your project
2. Click on a deployment
3. View "Build Logs" and "Function Logs"

### Analytics (Requires Pro Plan)

Vercel provides:
- Page views
- Top pages
- Referrers
- Device types
- Geographic data

Enable in: Project Settings → Analytics

---

## 🔒 Security Best Practices

1. **Never commit `.env` files** - Use Vercel env vars
2. **Use environment-specific API URLs**
3. **Enable HTTPS only** (Vercel default)
4. **Regularly update dependencies**:
   ```bash
   npm update
   npm audit fix
   ```
5. **Review Vercel security headers** in `vercel.json`

---

## ⚡ Performance Optimization

Your `vercel.json` already includes:
- ✅ Asset caching (1 year for immutable assets)
- ✅ SPA routing rewrites
- ✅ Vite optimization (code splitting, tree shaking)

Additional optimizations:
1. **Enable Vercel Analytics** for performance insights
2. **Use Vercel Image Optimization** for images
3. **Consider Server Components** for data-heavy pages

---

## 🎯 Production Checklist

Before going live:

- [ ] Backend deployed and stable
- [ ] CORS configured correctly
- [ ] Environment variables set
- [ ] Custom domain configured (if applicable)
- [ ] SSL certificate active (automatic with Vercel)
- [ ] Test all major features
- [ ] Check mobile responsiveness
- [ ] Review performance metrics
- [ ] Set up error monitoring (optional: Sentry)
- [ ] Document deployment process for team

---

## 🚀 Deployment Commands Reference

```bash
# Install Vercel CLI
npm install -g vercel

# Login
vercel login

# Preview deployment (from frontend directory)
cd frontend
vercel

# Production deployment
vercel --prod

# List deployments
vercel ls

# View logs
vercel logs

# Open project in dashboard
vercel

# Remove project
vercel remove <project-name>
```

---

## 📞 Support & Resources

- **Vercel Docs:** [vercel.com/docs](https://vercel.com/docs)
- **Vite Deployment:** [vitejs.dev/guide/static-deploy](https://vitejs.dev/guide/static-deploy.html)
- **Vercel Community:** [github.com/vercel/vercel/discussions](https://github.com/vercel/vercel/discussions)

---

## 🎉 Success!

Your InvestorLens AI frontend is now live on Vercel! 

**Next Steps:**
1. Share your deployment URL with stakeholders
2. Monitor deployment health
3. Set up continuous integration
4. Implement feature flags for safe deployments

**Deployed URL:** `https://your-project.vercel.app`

---

*Last updated: 2024*

