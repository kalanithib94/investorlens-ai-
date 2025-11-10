# 🚨 FIX CORS ERROR - Update Railway Backend

## Current Status:
- ✅ Frontend deployed: https://investorlens-ai.vercel.app
- ✅ Backend running: https://investorlens-ai-production.up.railway.app
- ❌ **CORS blocking connection!**

---

## 🎯 SOLUTION: Update CORS in Railway

### Step 1: Go to Railway

**Open**: https://railway.app

Log in if needed.

---

### Step 2: Select Your Project

1. Click on your project: **`investorlens-ai-`** or similar name

2. You should see two services:
   - Backend service (Python/FastAPI)
   - PostgreSQL database

3. **Click on the BACKEND service** (NOT the database!)

---

### Step 3: Go to Variables Tab

1. Click on the **"Variables"** tab (top of the page)

2. Look for a variable called: **`CORS_ORIGINS`**

---

### Step 4: Update CORS_ORIGINS

**Current value** (probably something like):
```json
["http://localhost:3000","http://localhost:5173"]
```

**Change it to** (copy this EXACTLY):
```json
["http://localhost:3000","http://localhost:5173","https://investorlens-ai.vercel.app","https://investorlens-ai-*.vercel.app"]
```

**How to edit:**
1. Click on `CORS_ORIGINS` variable
2. Click **"Edit"** or the pencil icon
3. **Replace the entire value** with the JSON above
4. Click **"Save"** or press Enter

---

### Step 5: Wait for Railway to Redeploy

After saving:
- Railway will **automatically redeploy** your backend (takes ~30 seconds)
- You'll see a deployment progress indicator
- Wait for it to show **"Active"** or **"Deployed"**

---

### Step 6: Test Your Frontend Again

1. **Go back to**: https://investorlens-ai.vercel.app

2. **Hard refresh** the page:
   - Windows: `Ctrl + Shift + R`
   - Mac: `Cmd + Shift + R`

3. **Check the result**:
   - ✅ Yellow warning banner should **disappear**
   - ✅ Dashboard should load with data
   - ✅ No CORS errors in console (F12)

---

## 📋 If CORS_ORIGINS Variable Doesn't Exist

**If you don't see `CORS_ORIGINS` in Railway Variables:**

1. Click **"New Variable"** button

2. Add:
   - **Name**: `CORS_ORIGINS`
   - **Value**: 
     ```json
     ["http://localhost:3000","http://localhost:5173","https://investorlens-ai.vercel.app","https://investorlens-ai-*.vercel.app"]
     ```

3. Click **"Add"**

4. Railway will redeploy automatically

---

## 🔍 Alternative: Check Backend Code

**If the variable exists but still not working**, we might need to check the backend code.

The CORS configuration should be in: `backend/app/main.py`

It should look like this:

```python
from fastapi.middleware.cors import CORSMiddleware
import json
import os

# CORS Configuration
cors_origins = json.loads(os.getenv("CORS_ORIGINS", '["http://localhost:3000"]'))

app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

## ✅ After Fix - Test Everything

### Test 1: Open Frontend
```
https://investorlens-ai.vercel.app
```

**Expected**:
- ✅ No warning banner
- ✅ Dashboard loads
- ✅ Data appears (or "No companies" if empty)

---

### Test 2: Browser Console (F12)

**Expected**:
- ✅ No CORS errors
- ✅ API calls succeed (200 OK)
- ✅ No red error messages

---

### Test 3: Share with Junior

**Send them**: https://investorlens-ai.vercel.app

They should:
- ✅ Access without login
- ✅ See the dashboard
- ✅ Everything works!

---

## 🎯 Summary

**The fix is simple:**

1. Go to Railway → Backend service → Variables
2. Add/Update `CORS_ORIGINS` to include your Vercel URL
3. Wait 30 seconds for redeploy
4. Refresh your frontend

**That's it!** 🚀

---

## 📞 Railway Variable Format (Reference)

**Correct format** (JSON array as string):
```json
["http://localhost:3000","http://localhost:5173","https://investorlens-ai.vercel.app","https://investorlens-ai-*.vercel.app"]
```

**Including the wildcard** (`https://investorlens-ai-*.vercel.app`) allows:
- All preview deployments to work
- Future branch deployments to work
- More flexibility

---

**Go fix CORS in Railway now! Should take 2 minutes! ⏱️**

