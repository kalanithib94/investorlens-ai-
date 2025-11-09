# Deploy to new GitHub repository: portfolio-intelligence
# PowerShell Script

Write-Host "🚀 Deploying to portfolio-intelligence repository" -ForegroundColor Cyan
Write-Host ""

# Get the new repository URL
Write-Host "Enter your new GitHub repository URL:" -ForegroundColor Yellow
Write-Host "Example: https://github.com/kalanithib94/portfolio-intelligence.git" -ForegroundColor Gray
$NEW_REPO_URL = Read-Host "URL"

Write-Host ""
Write-Host "📦 Adding new remote..." -ForegroundColor Blue
git remote add new-origin $NEW_REPO_URL

if ($LASTEXITCODE -ne 0) {
    Write-Host "Note: Remote might already exist, removing and re-adding..." -ForegroundColor Yellow
    git remote remove new-origin
    git remote add new-origin $NEW_REPO_URL
}

Write-Host ""
Write-Host "🔄 Pushing code to new repository..." -ForegroundColor Blue
git push new-origin main

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "✅ Code successfully pushed to portfolio-intelligence!" -ForegroundColor Green
    Write-Host ""
    Write-Host "📋 Next Steps:" -ForegroundColor Blue
    Write-Host "1. Deploy backend to Railway: https://railway.app/new" -ForegroundColor White
    Write-Host "2. Deploy frontend to Vercel: https://vercel.com/new" -ForegroundColor White
    Write-Host ""
    Write-Host "Repository URL: $NEW_REPO_URL" -ForegroundColor Green
} else {
    Write-Host ""
    Write-Host "❌ Push failed! Check the error above." -ForegroundColor Red
}

