# GitHub Setup Instructions for Docker Build

## Step 1: Create GitHub Repository

1. Go to https://github.com/new
2. Repository name: `deepseek-ocr-docker`
3. Make it **Public** (required for free GitHub Actions)
4. Click "Create repository"

---

## Step 2: Configure GitHub Secrets

1. In your new GitHub repo, go to **Settings** → **Secrets and variables** → **Actions**
2. Click **"New repository secret"**
3. Add these two secrets:

   **Secret 1:**
   - Name: `DOCKERHUB_USERNAME`
   - Value: `YOUR_DOCKERHUB_USERNAME`

   **Secret 2:**
   - Name: `DOCKERHUB_TOKEN`
   - Value: `YOUR_DOCKERHUB_TOKEN` (from Docker Hub → Account Settings → Security → New Access Token)

---

## Step 3: Push Code to GitHub

Open your terminal and run these commands:

```bash
cd "C:\Users\avniy\OneDrive\Desktop\websites\Docsi\deepseek-ocr-docker"

# Initialize git (if not already done)
git init

# Add GitHub remote (replace with your actual repo URL)
git remote add origin https://github.com/YOUR_USERNAME/deepseek-ocr-docker.git

# Stage all files
git add .

# Commit
git commit -m "Add DeepSeek-OCR Docker with GitHub Actions"

# Push to GitHub
git push -u origin main
```

If you get an error about "main" branch, try:
```bash
git branch -M main
git push -u origin main
```

---

## Step 4: Trigger the Build

Once you push to GitHub:

1. Go to your repo on GitHub
2. Click **"Actions"** tab
3. You should see the workflow running automatically
4. Wait 5-15 minutes for the build to complete

**OR manually trigger it:**
1. Go to **Actions** tab
2. Click **"Build and Push Docker Image"**
3. Click **"Run workflow"** → **"Run workflow"**

---

## Step 5: Verify Image on Docker Hub

1. Go to https://hub.docker.com/r/avniyayin1/deepseek-ocr-api
2. You should see your image with tag `latest`

---

## Step 6: Update RunPod

Once the Docker image is built and pushed:

1. Go to RunPod console
2. Edit your endpoint `deepseek-ocr-production`
3. Change Docker image to: `avniyayin1/deepseek-ocr-api:latest`
4. Set Max Workers to `3` (or more)
5. Save

---

## ✅ Done!

Your DeepSeek-OCR will now be available on RunPod serverless.

**Final image name:** `avniyayin1/deepseek-ocr-api:latest`
