# InvestorLens AI - Deployment Guide

## 🚀 Quick Deploy

This project is configured for easy deployment:

### Backend Deployment (Railway)

1. **Push to GitHub**:
```bash
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/yourusername/investorlens-ai.git
git push -u origin main
```

2. **Deploy to Railway**:
   - Go to [Railway.app](https://railway.app)
   - Click "New Project" → "Deploy from GitHub repo"
   - Select your repository
   - Railway will auto-detect the backend configuration
   - Add PostgreSQL database: Click "+ New" → "Database" → "PostgreSQL"
   - Set environment variables in Railway dashboard:
     - `DATABASE_URL` (auto-configured from PostgreSQL)
     - `OPENAI_API_KEY`
     - `SECRET_KEY`
     - `NEWS_API_KEY` (optional)
   - Deploy! 🎉

### Frontend Deployment (Vercel)

1. **Deploy to Vercel**:
   - Go to [Vercel.com](https://vercel.com)
   - Click "New Project" → Import from GitHub
   - Select your repository
   - Set root directory to `frontend`
   - Framework preset: Vite
   - Add environment variable:
     - `VITE_API_URL` = Your Railway backend URL
   - Deploy! 🎉

## 📦 Local Development

### Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

## 🔧 Environment Variables

### Backend (Railway)
- `DATABASE_URL` - PostgreSQL connection (auto-configured)
- `SECRET_KEY` - JWT secret key
- `OPENAI_API_KEY` - OpenAI API key for LLM features
- `NEWS_API_KEY` - NewsAPI key (optional)

### Frontend (Vercel)
- `VITE_API_URL` - Backend API URL from Railway

## 📊 Architecture

```
GitHub → Railway (Backend + PostgreSQL)
       ↓
     Vercel (Frontend)
```

## 🎯 Features Demonstrated

✅ **Cloud Deployment** (Railway, Vercel)  
✅ **CI/CD** (GitHub Actions)  
✅ **AI/LLM Integration** (OpenAI GPT-4, Claude)  
✅ **RESTful APIs** (25+ endpoints)  
✅ **Database** (PostgreSQL with SQLAlchemy)  
✅ **Modern Frontend** (React + Vite)  

## 📝 API Documentation

Once deployed, visit:
- Backend API Docs: `https://your-railway-app.up.railway.app/docs`
- Frontend App: `https://your-app.vercel.app`

## 🔗 Useful Links

- [Railway Documentation](https://docs.railway.app)
- [Vercel Documentation](https://vercel.com/docs)
- [FastAPI Documentation](https://fastapi.tiangolo.com)

