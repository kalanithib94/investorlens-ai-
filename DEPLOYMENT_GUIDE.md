# 🚀 Deployment Guide - InvestorLens AI

## Quick Deploy to Production (GitHub → Railway + Vercel)

### Prerequisites
- GitHub account
- Railway account (free tier: railway.app)
- Vercel account (free tier: vercel.com)
- OpenAI API key (optional, for AI features)

---

## Step 1: Push to GitHub (5 minutes)

```bash
# Navigate to project directory
cd Project

# Initialize git (if not already done)
git init
git add .
git commit -m "Initial commit: InvestorLens AI platform"

# Create repository on GitHub, then:
git remote add origin https://github.com/YOUR_USERNAME/investorlens-ai.git
git branch -M main
git push -u origin main
```

✅ **Your code is now on GitHub!**

---

## Step 2: Deploy Backend to Railway (10 minutes)

### 2.1 Create New Project
1. Go to [railway.app](https://railway.app)
2. Click "Start a New Project"
3. Select "Deploy from GitHub repo"
4. Choose your `investorlens-ai` repository
5. Select "Deploy Now"

### 2.2 Add PostgreSQL Database
1. In your Railway project, click "+ New"
2. Select "Database" → "PostgreSQL"
3. Wait for provisioning (1-2 minutes)
4. Railway automatically sets `DATABASE_URL` environment variable

### 2.3 Configure Environment Variables
In Railway project settings → Variables, add:

```
SECRET_KEY=your-random-secret-key-here
OPENAI_API_KEY=sk-your-openai-key
NEWS_API_KEY=your-newsapi-key (optional)
ANTHROPIC_API_KEY=your-anthropic-key (optional)
CORS_ORIGINS=https://your-app.vercel.app
```

**Generate SECRET_KEY:**
```python
import secrets
print(secrets.token_urlsafe(32))
```

### 2.4 Set Root Directory
1. Go to Settings → "Root Directory"
2. Set to: `backend`
3. Save

### 2.5 Get Your Backend URL
- Copy your Railway URL (e.g., `https://investorlens-backend-production.up.railway.app`)
- Test it: Visit `YOUR_URL/docs` to see API documentation

✅ **Backend is live!**

---

## Step 3: Deploy Frontend to Vercel (5 minutes)

### 3.1 Import Project
1. Go to [vercel.com](https://vercel.com)
2. Click "Add New" → "Project"
3. Import your GitHub repository
4. Framework Preset: **Vite** (auto-detected)
5. Root Directory: `frontend`

### 3.2 Set Environment Variable
Add this environment variable:

```
VITE_API_URL=https://your-railway-backend-url.up.railway.app
```
(Use your Railway URL from Step 2.5)

### 3.3 Deploy
1. Click "Deploy"
2. Wait 2-3 minutes for build
3. Get your Vercel URL (e.g., `https://investorlens-ai.vercel.app`)

✅ **Frontend is live!**

---

## Step 4: Initialize Database (2 minutes)

### Option A: Using Railway Terminal
1. Go to your Railway backend service
2. Click "Deployments" → Select latest deployment
3. Click "View Logs"
4. Open terminal and run:
```bash
python backend/scripts/init_db.py
```

### Option B: Using Local Script
```bash
cd backend
python scripts/init_db.py
```
(Make sure DATABASE_URL points to Railway database)

### Create Sample Data
When prompted, type `y` to create sample companies and alerts.

✅ **Database initialized with sample data!**

---

## Step 5: Test Your Deployment

### Backend Health Check
Visit: `https://your-railway-url.up.railway.app/health`

Should return:
```json
{
  "status": "healthy",
  "app_name": "InvestorLens AI",
  "version": "1.0.0"
}
```

### API Documentation
Visit: `https://your-railway-url.up.railway.app/docs`

You'll see interactive Swagger documentation for all 25+ endpoints!

### Frontend App
Visit: `https://your-vercel-url.vercel.app`

You should see the InvestorLens AI dashboard with sample companies!

---

## 🎯 Continuous Deployment (Automatic)

Now every time you push to GitHub:

**Main Branch:**
- Railway automatically rebuilds backend
- Vercel automatically rebuilds frontend
- Changes go live in 2-3 minutes

**Pull Requests:**
- Vercel creates preview deployment
- Railway can be configured for preview deployments
- Test before merging!

```bash
# Make changes
git add .
git commit -m "Add new feature"
git push origin main

# Wait 2-3 minutes → Changes are live! ✅
```

---

## 📊 Monitoring Your Application

### Railway Monitoring
- View logs: Railway Dashboard → Deployments → View Logs
- Monitor metrics: CPU, Memory, Network usage
- Set up alerts for downtime

### Vercel Analytics
- Built-in analytics (free)
- Real-time visitor stats
- Performance metrics

---

## 🔧 Local Development Setup

Want to run locally? Use Docker Compose:

```bash
# Clone and navigate
git clone https://github.com/YOUR_USERNAME/investorlens-ai.git
cd investorlens-ai/Project

# Set environment variables
cp backend/.env.example backend/.env
# Edit backend/.env with your API keys

# Start everything
docker-compose up

# Access:
# - Backend: http://localhost:8000
# - Frontend: http://localhost:3000
# - Database: localhost:5432
```

---

## 🎓 For Your Interview

### Demo the Live Application
1. Show the Vercel URL - live dashboard
2. Show Railway API docs - `/docs` endpoint
3. Explain the deployment pipeline:
   - "Push to GitHub"
   - "Automatic deployment to Railway and Vercel"
   - "CI/CD with automated testing"

### Technical Talking Points

**Architecture:**
- "Three-tier architecture: React frontend, FastAPI backend, PostgreSQL database"
- "Deployed on modern PaaS platforms for scalability"

**DevOps:**
- "Continuous deployment pipeline via GitHub"
- "Railway handles backend with automatic PostgreSQL provisioning"
- "Vercel optimizes frontend with edge network distribution"

**AI Integration:**
- "LLM integration with OpenAI GPT-4 and Anthropic Claude"
- "Risk scoring algorithm combining metrics and AI analysis"
- "Automated insights generation for portfolio monitoring"

**APIs:**
- "RESTful API with 25+ endpoints"
- "Auto-generated documentation with OpenAPI/Swagger"
- "External API integrations (NewsAPI, OpenAI, Claude)"

### Show Code Examples
Point to specific files that demonstrate skills:
- AI: `backend/app/services/ai_engine/llm_analyzer.py`
- APIs: `backend/app/api/companies.py`
- Testing: `backend/tests/integration/test_api.py`
- DevOps: `.github/workflows/ci-cd.yml`

---

## 🆘 Troubleshooting

### Backend Won't Start
- Check Railway logs for errors
- Verify DATABASE_URL is set
- Ensure all dependencies in requirements.txt

### Frontend Can't Connect to Backend
- Verify VITE_API_URL in Vercel settings
- Check CORS_ORIGINS in Railway backend
- Test backend health endpoint directly

### Database Connection Error
- PostgreSQL must be in same Railway project
- DATABASE_URL auto-set by Railway
- Run init_db.py after database is ready

### AI Features Not Working
- OPENAI_API_KEY must be valid
- Check Railway logs for API errors
- Fallback mode works without keys (mock data)

---

## 📈 Next Steps (Post-Interview Enhancements)

1. **Add Authentication**
   - Implement user login/registration
   - JWT token management already in place

2. **Add More Visualizations**
   - Time-series charts with Recharts
   - Portfolio performance heatmaps

3. **Implement Real-time Updates**
   - WebSocket for live alerts
   - Redis pub/sub for notifications

4. **Add Celery for Background Tasks**
   - Async AI processing
   - Scheduled portfolio analysis

5. **Custom Domain**
   - Vercel: Add custom domain in settings
   - Railway: Configure custom domain

---

## 🔗 Important URLs

Once deployed, bookmark these:

- **Frontend:** `https://your-app.vercel.app`
- **API Docs:** `https://your-railway-app.up.railway.app/docs`
- **Health Check:** `https://your-railway-app.up.railway.app/health`
- **GitHub Repo:** `https://github.com/YOUR_USERNAME/investorlens-ai`

---

## ✅ Deployment Checklist

- [ ] Code pushed to GitHub
- [ ] Railway project created
- [ ] PostgreSQL database provisioned
- [ ] Environment variables set in Railway
- [ ] Backend deployed and healthy
- [ ] Vercel project created
- [ ] VITE_API_URL configured
- [ ] Frontend deployed and accessible
- [ ] Database initialized with sample data
- [ ] API endpoints tested (/docs)
- [ ] Dashboard displays sample companies
- [ ] CI/CD pipeline verified (make test commit)

---

**Congratulations! Your InvestorLens AI platform is live! 🎉**

You now have a production-ready application demonstrating:
- ✅ Cloud deployment (Railway + Vercel)
- ✅ AI/LLM integration (GPT-4 + Claude)
- ✅ Complex RESTful APIs (25+ endpoints)
- ✅ Modern DevOps (CI/CD, containerization)
- ✅ Full-stack development (React + FastAPI)

Perfect for your KTP Associate interview at Sapphire Capital Partners! 🚀

