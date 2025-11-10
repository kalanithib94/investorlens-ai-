# 🚀 InvestorLens AI - Deployment Guide

**Simple, one-page guide for deploying your app**

---

## ✅ Current Status

- ✅ **Code**: Pushed to GitHub
- 🔄 **Railway**: Deploying backend (wait 1-2 min)
- 🔄 **Vercel**: Deploying frontend (wait 2-3 min)

---

## 🎯 Your URLs

| Service | URL |
|---------|-----|
| **Frontend** | https://investorlens-ai.vercel.app |
| **Backend** | https://investorlens-ai-production.up.railway.app |
| **GitHub** | https://github.com/kalanithib94/investorlens-ai-.git |

---

## ⚠️ IMPORTANT: Set Environment Variables

### 1. Vercel Environment Variable

**Go to**: https://vercel.com/kalanithib94s-projects/investorlens-ai/settings/environment-variables

Add this variable:
```
Name:  VITE_API_URL
Value: https://investorlens-ai-production.up.railway.app
Apply to: ✅ Production, Preview, Development (check all 3)
```

**After adding**, go to Deployments tab → Click latest → Redeploy (uncheck cache)

---

### 2. Railway Environment Variable

**Go to**: Railway dashboard → Backend service → Variables tab

Add this variable:
```
Name:  CORS_ORIGINS
Value: ["http://localhost:3000","http://localhost:5173","https://investorlens-ai.vercel.app","https://investorlens-ai-*.vercel.app"]
```

Railway will auto-redeploy after saving.

---

## ✅ Testing (After 5 Minutes)

### Test 1: Backend Health
Open: https://investorlens-ai-production.up.railway.app/health

**Should see**: `{"status":"healthy","app_name":"InvestorLens AI","version":"1.0.0"}`

### Test 2: Frontend
Open: https://investorlens-ai.vercel.app

**Should see**: 
- ✅ Dashboard loads
- ✅ No yellow warning banner
- ✅ "No companies in portfolio yet" (normal)

### Test 3: Console Check
Press F12 → Console tab

**Should NOT see**: 
- ❌ CORS errors
- ❌ Network errors

---

## 🐛 If Something's Wrong

### Problem: Yellow warning banner

**Fix**: Add `VITE_API_URL` to Vercel (see above), then redeploy

### Problem: CORS errors in console

**Fix**: Add `CORS_ORIGINS` to Railway (see above)

### Problem: Site requires Vercel login

**Fix**: Vercel → Settings → Deployment Protection → Set to "Off"

---

## 🎉 Success!

When working:
- Share URL with your team: https://investorlens-ai.vercel.app
- Anyone can access (no login needed)
- Dashboard loads properly

---

**That's it! Keep this file. Ignore all others.** 📋
