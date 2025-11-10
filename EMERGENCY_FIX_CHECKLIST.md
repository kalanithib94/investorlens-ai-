# 🚨 EMERGENCY FIX CHECKLIST
## InvestorLens AI - https://investorlens-ai.vercel.app/

**Status**: Site was working yesterday, now broken 😞

---

## 🔍 STEP 1: Diagnose the Problem

### Check Vercel Deployment Status

1. **Go to Vercel Dashboard**: https://vercel.com/kalanithib94s-projects/investorlens-ai
2. **Check Latest Deployment**:
   - Is it showing "Ready" (✅) or "Error" (❌)?
   - Click on the latest deployment
   - Look for build logs

**What you might see:**
- ✅ **"Ready"** but site broken → Environment variable issue or backend problem
- ❌ **"Error"** → Build failed, check logs
- ⚠️ **"Building"** → Wait for it to finish

---

## 🔍 STEP 2: Check Build Logs (If Build Failed)

1. Click on the failed deployment
2. Look at the **Build Logs**
3. Common errors:
   - `Module not found` → Missing dependency
   - `Command failed` → Build script issue
   - `Environment variable missing` → Config issue

---

## 🔍 STEP 3: Verify Environment Variables

**Go to**: https://vercel.com/kalanithib94s-projects/investorlens-ai/settings/environment-variables

**Check that this exists:**

| Name | Value | Environments |
|------|-------|--------------|
| `VITE_API_URL` | `https://investorlens-ai-production.up.railway.app` | ✅ Production, Preview, Development |

**⚠️ CRITICAL**: If this variable is missing or wrong, the frontend can't connect to backend!

**How to fix:**
1. If missing → Click "Add New" → Add it
2. If wrong → Edit it
3. After changing → Redeploy (Settings → Deployments → Latest → Redeploy)

---

## 🔍 STEP 4: Test Backend Health

**Open this URL**: https://investorlens-ai-production.up.railway.app/health

**Expected Response:**
```json
{
  "status": "healthy",
  "app_name": "InvestorLens AI",
  "version": "1.0.0"
}
```

**If backend is down:**
- 🔴 Error or timeout → Backend crashed
- 🔴 404 or 502 → Backend deployment issue
- ✅ Returns JSON above → Backend is fine!

**If backend is down, go to Railway:**
1. https://railway.app
2. Check if service is running
3. Look at deployment logs
4. Redeploy if needed

---

## 🔍 STEP 5: Check Vercel Build Settings

**Go to**: https://vercel.com/kalanithib94s-projects/investorlens-ai/settings/general

**Verify these settings:**

| Setting | Value |
|---------|-------|
| **Framework Preset** | Vite |
| **Root Directory** | `frontend` |
| **Build Command** | `npm run build` |
| **Output Directory** | `dist` |
| **Install Command** | `npm install` |

**If any are wrong:**
1. Click "Edit" next to the setting
2. Fix it
3. Click "Save"
4. Go to Deployments → Redeploy

---

## 🔍 STEP 6: Check for Recent Commits

**Did you push any code changes today?**

Run this command to see recent commits:
```powershell
git log --oneline -5
```

**If you see unexpected commits:**
- Check what changed: `git show <commit-hash>`
- Revert if needed: `git revert <commit-hash>` then `git push`

---

## 🔍 STEP 7: Check Browser Console

1. **Open your site**: https://investorlens-ai.vercel.app/
2. **Press F12** → Go to **Console** tab
3. **Look for errors**:

**Common errors:**

| Error | Meaning | Fix |
|-------|---------|-----|
| `Failed to fetch` | Can't reach backend | Check backend URL and CORS |
| `CORS error` | Backend blocking frontend | Update CORS in Railway |
| `404 for /api/companies` | API endpoint not found | Backend route issue |
| `Uncaught TypeError` | JavaScript error | Code bug, check build |
| Blank/white screen | Build or routing issue | Check build logs |

---

## ✅ QUICK FIXES (Try These First!)

### Quick Fix #1: Redeploy Frontend

**Sometimes Vercel just needs a fresh deployment:**

```powershell
cd frontend
git commit --allow-empty -m "Force redeploy"
git push origin main
```

Then wait 2-3 minutes and check: https://investorlens-ai.vercel.app/

---

### Quick Fix #2: Verify & Redeploy with Environment Variable

1. **Go to Vercel**: https://vercel.com/kalanithib94s-projects/investorlens-ai/settings/environment-variables

2. **Check `VITE_API_URL`** exists with value:
   ```
   https://investorlens-ai-production.up.railway.app
   ```

3. **If it's there but site is broken**:
   - Go to Deployments tab
   - Click latest deployment "..." menu
   - Click **"Redeploy"**
   - ✅ Check "Use existing build cache" is OFF
   - Click "Redeploy"

---

### Quick Fix #3: Check Root Directory

**This is the #1 cause of broken deployments!**

1. **Go to**: https://vercel.com/kalanithib94s-projects/investorlens-ai/settings/general
2. **Check "Root Directory"** → Should say: `frontend`
3. **If it's empty or says something else**:
   - Click "Edit"
   - Type: `frontend`
   - Click "Save"
   - Redeploy

---

### Quick Fix #4: Test Backend is Alive

**Open these URLs and verify they work:**

1. **Health Check**: https://investorlens-ai-production.up.railway.app/health
   - Should return JSON: `{"status":"healthy",...}`

2. **API Docs**: https://investorlens-ai-production.up.railway.app/docs
   - Should show Swagger UI

3. **Companies API**: https://investorlens-ai-production.up.railway.app/api/companies
   - Should return JSON array (might be empty, that's okay)

**If ANY of these fail:**
- Backend is down or misconfigured
- Go to Railway: https://railway.app
- Check deployment status
- Check logs for errors

---

### Quick Fix #5: Update CORS (If You See CORS Errors)

**If browser console shows CORS errors:**

1. **Go to Railway**: https://railway.app
2. **Select backend service**
3. **Go to Variables tab**
4. **Find `CORS_ORIGINS`**
5. **Make sure it includes**:
   ```json
   ["http://localhost:3000","http://localhost:5173","https://investorlens-ai.vercel.app","https://investorlens-ai-*.vercel.app"]
   ```
6. **Save** → Railway will auto-redeploy

---

## 🎯 MOST LIKELY CAUSES (Based on "It Worked Yesterday")

1. **❌ Environment variable got deleted in Vercel**
   - Fix: Re-add `VITE_API_URL` and redeploy

2. **❌ Backend crashed or went to sleep**
   - Fix: Wake up Railway backend by visiting the health endpoint

3. **❌ Recent commit broke something**
   - Fix: Check git log and revert bad commit

4. **❌ Vercel changed a setting automatically**
   - Fix: Verify Root Directory is still `frontend`

5. **❌ CORS got misconfigured**
   - Fix: Re-add Vercel URL to Railway CORS settings

---

## 📝 Report Back What You Find

After checking the steps above, tell me:

1. **Vercel deployment status**: Ready / Error / Building?
2. **Environment variable `VITE_API_URL`**: Present / Missing?
3. **Backend health check**: Working / Failing?
4. **Browser console**: Any errors?
5. **Root Directory setting**: `frontend` / Something else?

This will help me pinpoint the exact issue! 🔧

---

## 🚀 Nuclear Option (If Nothing Works)

**If all else fails, delete and recreate the Vercel project:**

1. **Delete**: https://vercel.com/kalanithib94s-projects/investorlens-ai/settings
   - Scroll to bottom → Delete Project

2. **Recreate**: https://vercel.com/new
   - Import: `kalanithib94/investorlens-ai-`
   - Root Directory: `frontend`
   - Framework: Vite
   - Add env var: `VITE_API_URL` = `https://investorlens-ai-production.up.railway.app`
   - Deploy

**Takes 5 minutes and guarantees a clean slate!**

---

**Good luck! 🍀 Report back what you find!**

