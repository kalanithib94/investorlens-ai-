# 🚀 Quick Fix Guide - Connect Frontend to Backend

## ✅ Current Status

**Frontend (Vercel)**: https://investorlens-ai-pgy3.vercel.app ✅ DEPLOYED  
**Backend (Railway)**: https://investorlens-ai-production.up.railway.app ✅ DEPLOYED  
**Database**: PostgreSQL ✅ CONNECTED

**Issue**: Frontend can't reach backend (needs configuration)

---

## 🔧 Step 1: Add Variables in Railway (You're Here Now!)

You're on the right screen! Click **"+ New Variable"** and add:

### Variable 1: SECRET_KEY
```
Name: SECRET_KEY
Value: django-insecure-change-this-random-string-in-production-abc123xyz789
```

### Variable 2: CORS_ORIGINS (CRITICAL!)
```
Name: CORS_ORIGINS
Value: ["http://localhost:3000","http://localhost:5173","https://investorlens-ai-pgy3.vercel.app","https://investorlens-ai-pgy3-*.vercel.app"]
```

### Variable 3: DEBUG
```
Name: DEBUG
Value: False
```

**After adding, Railway will automatically redeploy (wait 2 minutes)**

---

## 🔗 Step 2: Update Vercel with Backend URL

1. Go to: https://vercel.com/dashboard
2. Click on: `investorlens-ai-pgy3` project
3. Go to: **Settings** → **Environment Variables**
4. Click: **Add New**
5. Enter:
   - **Key**: `VITE_API_URL`
   - **Value**: `https://investorlens-ai-production.up.railway.app`
   - **Environments**: Select ALL (Production, Preview, Development)
6. Click **Save**
7. Go to **Deployments** tab
8. Find latest deployment → Click **"..."** → **Redeploy**

---

## 🧪 Step 3: Test Backend Health

Open this URL in browser:
```
https://investorlens-ai-production.up.railway.app/health
```

You should see:
```json
{
  "status": "healthy",
  "app_name": "InvestorLens AI",
  "version": "1.0.0"
}
```

If you see this, backend is working! ✅

---

## 🎯 Step 4: Test Complete Integration

1. Visit: https://investorlens-ai-pgy3.vercel.app
2. Open Browser DevTools (F12)
3. Check Console - should have NO red errors
4. Check Network tab - API calls should succeed

**Expected Result**: 
- No warning banner
- Dashboard loads properly
- May be empty (no data added yet)

---

## ⚠️ Troubleshooting

### If backend health check fails:
- Check Railway deployment logs
- Verify all environment variables are added
- Wait for Railway to finish redeploying

### If CORS errors persist:
- Double-check CORS_ORIGINS in Railway includes your Vercel URL
- Make sure to include both URLs:
  - `https://investorlens-ai-pgy3.vercel.app`
  - `https://investorlens-ai-pgy3-*.vercel.app`
- Redeploy Railway backend after fixing

### If frontend still shows error:
- Verify VITE_API_URL is set in Vercel
- Redeploy Vercel after adding env var
- Clear browser cache and reload

---

## ✅ Success Checklist

- [ ] SECRET_KEY added to Railway
- [ ] CORS_ORIGINS added to Railway (with Vercel URLs)
- [ ] DEBUG=False added to Railway
- [ ] Railway backend redeployed
- [ ] Backend health check returns 200 OK
- [ ] VITE_API_URL added to Vercel
- [ ] Vercel frontend redeployed
- [ ] Frontend loads without warning
- [ ] No CORS errors in browser console

---

## 📊 Your URLs

```
GitHub:   https://github.com/kalanithib94/investorlens-ai-.git
Railway:  https://investorlens-ai-production.up.railway.app
Vercel:   https://investorlens-ai-pgy3.vercel.app
```

---

**Complete these steps and your app will be fully connected! 🎉**

