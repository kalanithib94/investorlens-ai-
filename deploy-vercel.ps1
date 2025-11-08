# Deploy Frontend to Vercel - PowerShell Script
# InvestorLens AI Deployment Automation

Write-Host "🚀 InvestorLens AI - Vercel Deployment" -ForegroundColor Cyan
Write-Host "=======================================" -ForegroundColor Cyan
Write-Host ""

# Check if we're in the right directory
if (-not (Test-Path "frontend")) {
    Write-Host "❌ Error: Must run from project root directory!" -ForegroundColor Red
    exit 1
}

# Navigate to frontend
Set-Location frontend

Write-Host "📦 Step 1: Checking Vercel CLI..." -ForegroundColor Yellow
$vercelInstalled = Get-Command vercel -ErrorAction SilentlyContinue
if (-not $vercelInstalled) {
    Write-Host "❌ Vercel CLI not installed. Installing..." -ForegroundColor Red
    npm install -g vercel
    Write-Host "✅ Vercel CLI installed!" -ForegroundColor Green
} else {
    Write-Host "✅ Vercel CLI found!" -ForegroundColor Green
}

Write-Host ""
Write-Host "🔐 Step 2: Login to Vercel..." -ForegroundColor Yellow
Write-Host "   (Browser window will open for authentication)" -ForegroundColor Gray
vercel login

if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Vercel login failed!" -ForegroundColor Red
    Set-Location ..
    exit 1
}

Write-Host ""
Write-Host "✅ Logged in successfully!" -ForegroundColor Green
Write-Host ""

Write-Host "🏗️  Step 3: Building and deploying to production..." -ForegroundColor Yellow
Write-Host "   This may take 2-3 minutes..." -ForegroundColor Gray
Write-Host ""

vercel --prod --yes

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "🎉 DEPLOYMENT SUCCESSFUL!" -ForegroundColor Green
    Write-Host "=======================================" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "✅ Your frontend is now live on Vercel!" -ForegroundColor Green
    Write-Host ""
    Write-Host "📋 Next Steps:" -ForegroundColor Yellow
    Write-Host "   1. Note your deployment URL (shown above)" -ForegroundColor White
    Write-Host "   2. Add VITE_API_URL environment variable in Vercel Dashboard:" -ForegroundColor White
    Write-Host "      → Go to: https://vercel.com/dashboard" -ForegroundColor Gray
    Write-Host "      → Select your project" -ForegroundColor Gray
    Write-Host "      → Settings → Environment Variables" -ForegroundColor Gray
    Write-Host "      → Add: VITE_API_URL = your-railway-backend-url" -ForegroundColor Gray
    Write-Host "   3. Update backend CORS with your Vercel URL" -ForegroundColor White
    Write-Host "   4. Test your deployment!" -ForegroundColor White
    Write-Host ""
    Write-Host "📚 Documentation: frontend/VERCEL_DEPLOYMENT.md" -ForegroundColor Cyan
    Write-Host ""
} else {
    Write-Host ""
    Write-Host "❌ Deployment failed!" -ForegroundColor Red
    Write-Host "   Check the error messages above." -ForegroundColor Yellow
    Write-Host "   Need help? See: frontend/VERCEL_DEPLOYMENT.md" -ForegroundColor Cyan
    Write-Host ""
    Set-Location ..
    exit 1
}

Set-Location ..
Write-Host "✅ Done!" -ForegroundColor Green

