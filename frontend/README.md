# 🎯 InvestorLens AI - Frontend

Modern React + Vite frontend for the InvestorLens AI Portfolio Intelligence Platform.

## 🚀 Quick Start

### Prerequisites

- Node.js 18+ and npm
- Backend API running (local or deployed)

### Local Development

1. **Install dependencies:**
   ```bash
   npm install
   ```

2. **Configure environment variables:**
   
   Copy `env.example` to `.env.local`:
   ```bash
   cp env.example .env.local
   ```
   
   Update `.env.local`:
   ```env
   VITE_API_URL=http://localhost:8000
   ```

3. **Start development server:**
   ```bash
   npm run dev
   ```
   
   App will be available at `http://localhost:3000`

4. **Build for production:**
   ```bash
   npm run build
   ```
   
   Output will be in `dist/` directory.

5. **Preview production build:**
   ```bash
   npm run preview
   ```

---

## 📁 Project Structure

```
frontend/
├── public/              # Static assets
├── src/
│   ├── components/      # React components
│   │   ├── Dashboard/   # Main dashboard
│   │   ├── CompanyCard/ # Company display card
│   │   └── AlertPanel/  # Alerts panel
│   ├── pages/          # Page components (future)
│   ├── services/       # API services
│   │   └── api.js      # API client & endpoints
│   ├── App.jsx         # Root component
│   ├── main.jsx        # Entry point
│   └── index.css       # Global styles
├── index.html          # HTML template
├── vite.config.js      # Vite configuration
├── tailwind.config.js  # Tailwind CSS config
├── vercel.json         # Vercel deployment config
└── package.json        # Dependencies
```

---

## 🛠️ Technology Stack

- **Framework:** React 18.3
- **Build Tool:** Vite 5.4
- **Styling:** Tailwind CSS 3.4
- **Icons:** Lucide React
- **HTTP Client:** Axios
- **Charts:** Recharts
- **Date Formatting:** date-fns
- **State Management:** Zustand (optional)
- **Data Fetching:** TanStack Query (optional)

---

## 🎨 Key Features

### Dashboard
- Portfolio overview with key metrics
- Real-time company monitoring
- Risk score visualization
- Alert notifications

### Components
- **CompanyCard**: Displays company info, metrics, and risk scores
- **AlertPanel**: Shows active alerts with severity indicators
- **Dashboard**: Main portfolio view with stats and company grid

### API Integration
- Centralized API client with Axios
- Automatic JWT token management
- Request/response interceptors
- Error handling

---

## 🔧 Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `VITE_API_URL` | Backend API URL | `http://localhost:8000` |
| `VITE_DEBUG` | Enable debug logging | `false` |

### Vite Configuration

```javascript
// vite.config.js
{
  server: {
    port: 3000,
    proxy: {
      '/api': {
        target: process.env.VITE_API_URL || 'http://localhost:8000',
        changeOrigin: true
      }
    }
  }
}
```

### Tailwind Configuration

Custom color palette with primary, success, warning, and danger colors.

```javascript
// tailwind.config.js - Already configured ✅
```

---

## 📝 Available Scripts

| Command | Description |
|---------|-------------|
| `npm run dev` | Start development server (port 3000) |
| `npm run build` | Build for production |
| `npm run preview` | Preview production build |
| `npm run lint` | Run ESLint |

---

## 🌐 Deployment

### Deploy to Vercel (Recommended)

**Quick Deploy:**
```bash
cd frontend
vercel
```

**Production Deploy:**
```bash
vercel --prod
```

**Via GitHub:**
1. Push to GitHub
2. Import to Vercel
3. Set Root Directory to `frontend`
4. Add `VITE_API_URL` environment variable
5. Deploy!

👉 **[Full Deployment Guide](./VERCEL_DEPLOYMENT.md)**

### Deploy to Other Platforms

The frontend is a static SPA that can be deployed anywhere:

- **Netlify:** Connect GitHub repo, set build command `npm run build`, publish directory `dist`
- **Cloudflare Pages:** Same as Netlify
- **AWS S3 + CloudFront:** Upload `dist/` contents
- **GitHub Pages:** Use `vite-plugin-pages` plugin

---

## 🔌 API Integration

### API Service Structure

```javascript
// src/services/api.js

// Companies API
companiesAPI.getAll()
companiesAPI.getById(id)
companiesAPI.getNews(id)
companiesAPI.getInsights(id)

// Analysis API
analysisAPI.generateSummary(companyId)
analysisAPI.calculateRiskScore(companyId)

// Alerts API
alertsAPI.getAll()
alertsAPI.markRead(id)
alertsAPI.getStats()
```

### Using in Components

```javascript
import { companiesAPI } from '../services/api';

const fetchData = async () => {
  const companies = await companiesAPI.getAll();
  setCompanies(companies);
};
```

---

## 🎨 Styling Guide

### Tailwind Utility Classes

Custom classes available:

```css
/* Cards */
.card

/* Buttons */
.btn-primary
.btn-secondary

/* Badges */
.badge
.badge-success
.badge-warning
.badge-danger
```

### Color Palette

- **Primary:** Blue (#2563eb)
- **Success:** Green (#22c55e)
- **Warning:** Yellow (#f59e0b)
- **Danger:** Red (#ef4444)

---

## 🧪 Testing

Currently no tests configured. Recommended additions:

```bash
# Install testing dependencies
npm install -D vitest @testing-library/react @testing-library/jest-dom

# Add test script to package.json
"test": "vitest"
```

---

## 🐛 Troubleshooting

### Common Issues

**1. API Connection Fails**
- Check `VITE_API_URL` is set correctly
- Ensure backend is running
- Check CORS configuration in backend

**2. Build Fails**
- Clear node_modules: `rm -rf node_modules && npm install`
- Clear Vite cache: `rm -rf node_modules/.vite`

**3. Styles Not Applying**
- Ensure Tailwind is configured correctly
- Check `index.css` imports Tailwind directives
- Rebuild: `npm run build`

**4. Hot Reload Not Working**
- Restart dev server
- Check file watch limits (Linux): `echo fs.inotify.max_user_watches=524288 | sudo tee -a /etc/sysctl.conf`

---

## 📦 Dependencies Update

Update dependencies:

```bash
# Check outdated packages
npm outdated

# Update all to latest
npm update

# Audit security vulnerabilities
npm audit
npm audit fix
```

---

## 🔐 Security

- Never commit `.env` files
- Use environment variables for sensitive data
- Keep dependencies updated
- Review `npm audit` regularly
- Use HTTPS in production

---

## 🤝 Contributing

When adding new features:

1. Create new components in `src/components/`
2. Add API endpoints in `src/services/api.js`
3. Follow existing code structure
4. Use Tailwind for styling
5. Test locally before committing

---

## 📞 Support

- **Documentation:** See [VERCEL_DEPLOYMENT.md](./VERCEL_DEPLOYMENT.md)
- **Issues:** Check console for errors
- **Backend API:** Ensure backend is running and accessible

---

## 📄 License

Part of InvestorLens AI Portfolio Intelligence Platform

---

## 🎯 Next Steps

- [ ] Add authentication (JWT)
- [ ] Implement routing with React Router
- [ ] Add company detail pages
- [ ] Create company addition form
- [ ] Add data visualization (charts)
- [ ] Implement real-time updates (WebSocket)
- [ ] Add user settings
- [ ] Implement dark mode
- [ ] Add unit tests
- [ ] Add E2E tests with Playwright

---

**Built with ❤️ using React + Vite + Tailwind CSS**

