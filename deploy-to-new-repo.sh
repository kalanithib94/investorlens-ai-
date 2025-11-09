#!/bin/bash
# Deploy to new GitHub repository: portfolio-intelligence

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${BLUE}🚀 Deploying to portfolio-intelligence repository${NC}"
echo ""

# Get the new repository URL
echo -e "${YELLOW}Enter your new GitHub repository URL:${NC}"
echo "Example: https://github.com/kalanithib94/portfolio-intelligence.git"
read NEW_REPO_URL

echo ""
echo -e "${BLUE}📦 Adding new remote...${NC}"
git remote add new-origin $NEW_REPO_URL

echo ""
echo -e "${BLUE}🔄 Pushing code to new repository...${NC}"
git push new-origin main

echo ""
echo -e "${GREEN}✅ Code successfully pushed to portfolio-intelligence!${NC}"
echo ""
echo -e "${BLUE}📋 Next Steps:${NC}"
echo "1. Deploy backend to Railway: https://railway.app/new"
echo "2. Deploy frontend to Vercel: https://vercel.com/new"
echo ""
echo -e "${GREEN}Repository URL: $NEW_REPO_URL${NC}"

