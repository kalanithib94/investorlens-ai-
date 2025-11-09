# 🚀 Brand New Deployment - Fresh Everything

**Creating entirely new projects with all lessons learned**

---

## 📋 What We'll Create

- ✅ New GitHub Repository
- ✅ New Railway Project (Backend + Database)
- ✅ New Vercel Project (Frontend)
- ✅ Test with Puppeteer

---

## Phase 1: Create New GitHub Repository

### Step 1: Create New Repo on GitHub

1. Go to: https://github.com/new
2. **Repository name**: `investorlens-ai-v2` (or your choice)
3. **Description**: "InvestorLens AI - Portfolio Intelligence Platform"
4. **Visibility**: Public or Private (your choice)
5. **DO NOT initialize** with README, .gitignore, or license
6. Click **"Create repository"**
7. **Copy the repository URL** (e.g., `https://github.com/yourusername/investorlens-ai-v2.git`)

---

## Phase 2: Push Code to New Repository

I'll do this for you automatically.

---

## Phase 3: Deploy Backend to Railway (New Project)

### Step 1: Create New Railway Project

1. Go to: https://railway.app/new
2. Click **"Deploy from GitHub repo"**
3. Select your NEW repository: `investorlens-ai-v2`
4. Railway will auto-detect Python app
5. Wait for initial deployment

### Step 2: Add PostgreSQL Database

1. In your Railway project, click **"+ New"**
2. Select **"Database"** → **"Add PostgreSQL"**
3. Railway automatically creates and links `DATABASE_URL`

### Step 3: Configure Variables

Click on backend service → **Variables** → Add these:

```
SECRET_KEY=sk-investorlens-fresh-7x9mK2pL4nQ8wR5tY3vN6aJ1bC0dE9fG2hM4jP7sU
DEBUG=False
PORT=8000
CORS_ORIGINS=["http://localhost:3000","http://localhost:5173"]
```

**Note**: We'll update CORS_ORIGINS after getting Vercel URL

### Step 4: Generate Domain

1. Click backend service → **Settings**
2. Scroll to **"Networking"**
3. Click **"Generate Domain"**
4. **Copy the URL** (e.g., `https://your-new-app.up.railway.app`)

---

## Phase 4: Deploy Frontend to Vercel (New Project)

### Step 1: Import to Vercel

1. Go to: https://vercel.com/new
2. Click **"Add New..."** → **"Project"**
3. Import your NEW repository: `investorlens-ai-v2`
4. Click **"Import"**

### Step 2: Configure Settings

**CRITICAL - Set these exactly:**

```
Framework Preset: Vite
Root Directory: frontend          ⚠️ MUST SET THIS!
Build Command: npm run build
Output Directory: dist
Install Command: npm install
```

### Step 3: Add Environment Variable

Before deploying, add:

```
Name: VITE_API_URL
Value: https://your-new-railway-url.up.railway.app
Environments: ✅ Production, ✅ Preview, ✅ Development
```

### Step 4: Deploy

1. Click **"Deploy"**
2. Wait 2-3 minutes
3. Copy your Vercel URL (e.g., `https://your-new-project.vercel.app`)

---

## Phase 5: Update Backend CORS

1. Go back to Railway
2. Backend service → **Variables**
3. Update **CORS_ORIGINS** to:

```json
["http://localhost:3000","http://localhost:5173","https://your-vercel-url.vercel.app","https://your-vercel-url-*.vercel.app"]
```

4. Save (Railway auto-redeploys)

---

## Phase 6: Test with Puppeteer

I'll run comprehensive tests to verify everything works.

---

## 📊 Checklist

- [ ] New GitHub repo created
- [ ] Code pushed to new repo
- [ ] Railway project created
- [ ] PostgreSQL added to Railway
- [ ] Environment variables set in Railway
- [ ] Railway domain generated
- [ ] Vercel project created
- [ ] Root Directory set to `frontend`
- [ ] VITE_API_URL set in Vercel
- [ ] Vercel deployment successful
- [ ] CORS updated in Railway
- [ ] Puppeteer tests passing

---

## 🎯 Your New URLs

```
GitHub:   https://github.com/___________/investorlens-ai-v2
Railway:  https://__________________.up.railway.app
Vercel:   https://__________________.vercel.app
```

---

**Ready to start? Tell me the name you want for the new GitHub repo!**

