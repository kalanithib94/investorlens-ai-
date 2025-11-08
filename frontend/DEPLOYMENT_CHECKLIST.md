# ✅ Vercel Deployment Checklist - InvestorLens AI

Use this checklist to ensure a smooth deployment to Vercel.

## 🎯 Pre-Deployment (Do This First)

- [ ] **Backend is deployed and running**
  - [ ] Backend URL available (e.g., `https://your-app.up.railway.app`)
  - [ ] Backend health check working (`/health` endpoint)
  - [ ] Backend API accessible

- [ ] **Local build test passes**
  ```bash
  cd frontend
  npm install
  npm run build
  ```
  - [ ] Build completes without errors
  - [ ] No TypeScript/ESLint errors

- [ ] **Environment variables prepared**
  - [ ] Backend URL ready to add to Vercel
  - [ ] Format: `https://your-backend-url.com` (no trailing slash)

---

## 🚀 Deployment Steps

### Option 1: Via Vercel CLI (Quick)

- [ ] **Install Vercel CLI**
  ```bash
  npm install -g vercel
  ```

- [ ] **Login to Vercel**
  ```bash
  vercel login
  ```

- [ ] **Deploy (from frontend directory)**
  ```bash
  cd frontend
  vercel
  ```

- [ ] **Configure on first deployment**
  - [ ] Project name: `investorlens-frontend` (or custom)
  - [ ] Directory: `./` (current)
  - [ ] Settings detected: ✅

- [ ] **Add environment variable**
  ```bash
  vercel env add VITE_API_URL
  ```
  Enter your backend URL when prompted

- [ ] **Deploy to production**
  ```bash
  vercel --prod
  ```

### Option 2: Via GitHub + Dashboard (Recommended)

- [ ] **Push to GitHub**
  ```bash
  git add .
  git commit -m "Ready for Vercel deployment"
  git push origin main
  ```

- [ ] **Import to Vercel**
  - [ ] Go to [vercel.com/new](https://vercel.com/new)
  - [ ] Import your GitHub repository
  - [ ] Select repository

- [ ] **Configure project**
  - [ ] Framework: **Vite** ✅
  - [ ] Root Directory: **`frontend`** ⚠️ IMPORTANT!
  - [ ] Build Command: `npm run build` (auto-detected)
  - [ ] Output Directory: `dist` (auto-detected)

- [ ] **Add environment variables**
  - [ ] Click "Environment Variables"
  - [ ] Add: `VITE_API_URL` = `https://your-backend-url.com`
  - [ ] Apply to: Production, Preview, Development ✅

- [ ] **Click "Deploy"**
  - [ ] Wait 2-3 minutes for build
  - [ ] Deployment successful ✅

---

## 🔧 Post-Deployment Configuration

- [ ] **Update Backend CORS**
  
  **In Railway (or your backend host):**
  1. [ ] Go to Backend Service → Variables
  2. [ ] Update `CORS_ORIGINS` to include:
     ```
     ["http://localhost:3000","http://localhost:5173","https://your-app.vercel.app","https://your-app-*.vercel.app"]
     ```
  3. [ ] Save and redeploy backend

- [ ] **Test Deployment**
  - [ ] Open Vercel URL in browser
  - [ ] Open DevTools Console (F12)
  - [ ] Check for errors:
    - [ ] No CORS errors
    - [ ] No API connection errors
    - [ ] No 404 errors
  - [ ] Test functionality:
    - [ ] Dashboard loads
    - [ ] Data displays (if backend has data)
    - [ ] No visual glitches

- [ ] **Test API Connectivity**
  - [ ] Check Network tab in DevTools
  - [ ] API requests going to correct URL
  - [ ] Status codes: 200 OK (or expected codes)
  - [ ] Response data valid

---

## 📊 Verify Deployment

- [ ] **Check Deployment Status**
  - [ ] Visit Vercel Dashboard → Deployments
  - [ ] Status: "Ready" ✅
  - [ ] No build errors

- [ ] **Review Build Logs**
  - [ ] Click on deployment
  - [ ] Check "Build Logs" for warnings
  - [ ] All steps completed successfully

- [ ] **Test on Multiple Devices**
  - [ ] Desktop browser
  - [ ] Mobile browser
  - [ ] Different browsers (Chrome, Firefox, Safari)

- [ ] **Performance Check**
  - [ ] Page loads quickly
  - [ ] No console errors
  - [ ] Images/assets load properly

---

## 🎯 Optional Enhancements

- [ ] **Custom Domain**
  - [ ] Go to Project → Settings → Domains
  - [ ] Add custom domain
  - [ ] Update DNS records
  - [ ] Verify SSL certificate
  - [ ] Update backend CORS with custom domain

- [ ] **Analytics**
  - [ ] Enable Vercel Analytics (if on Pro plan)
  - [ ] Set up error tracking (e.g., Sentry)

- [ ] **Performance**
  - [ ] Run Lighthouse audit
  - [ ] Check Core Web Vitals
  - [ ] Optimize if needed

---

## 🐛 Troubleshooting

If something goes wrong, check:

- [ ] **Build fails**
  - [ ] Root Directory set to `frontend`? ✅
  - [ ] All dependencies in package.json?
  - [ ] Test build locally: `npm run build`

- [ ] **Blank page**
  - [ ] Check Console for JavaScript errors
  - [ ] Verify `VITE_API_URL` is set
  - [ ] Check Network tab for failed requests

- [ ] **CORS errors**
  - [ ] Backend CORS includes Vercel domain?
  - [ ] Backend redeployed after CORS update?
  - [ ] Try clearing browser cache

- [ ] **API calls fail**
  - [ ] Correct backend URL in `VITE_API_URL`?
  - [ ] Backend running and accessible?
  - [ ] Test backend directly: `curl https://backend-url/health`

- [ ] **Environment variables not working**
  - [ ] Variables set in Vercel Dashboard?
  - [ ] Applied to all environments?
  - [ ] **Redeployed after adding variables?** (Required!)

---

## 📝 Post-Launch

- [ ] **Documentation**
  - [ ] Note deployment URL
  - [ ] Update team documentation
  - [ ] Save environment variable values securely

- [ ] **Monitoring**
  - [ ] Set up uptime monitoring
  - [ ] Configure error alerts
  - [ ] Review deployment logs regularly

- [ ] **Team Access**
  - [ ] Add team members to Vercel project
  - [ ] Set appropriate permissions
  - [ ] Share deployment URL

---

## ✅ Deployment Complete!

**Your app is live! 🎉**

- **Deployment URL:** `https://__________________.vercel.app`
- **Backend URL:** `https://__________________.railway.app`
- **Deployment Date:** `__________`

**Next Steps:**
1. Share URL with stakeholders
2. Monitor for errors
3. Collect user feedback
4. Iterate and improve

---

## 🆘 Need Help?

- **Vercel Status:** [vercel-status.com](https://www.vercel-status.com)
- **Vercel Docs:** [vercel.com/docs](https://vercel.com/docs)
- **Full Guide:** See [VERCEL_DEPLOYMENT.md](./VERCEL_DEPLOYMENT.md)

---

**Last Updated:** 2024

