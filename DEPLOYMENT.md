# CampusVault Deployment Guide

## Backend Deployment

### Option 1: Deploy on Render

1. Push code to GitHub
2. Connect GitHub repo to Render
3. Set environment variables in Render:
   ```
   FIREBASE_CREDENTIALS=<json-content>
   SECRET_KEY=<your-secret>
   OPENAI_API_KEY=<your-key>
   ```
4. Set build command: `pip install -r requirements.txt`
5. Set start command: `uvicorn app.main:app --host 0.0.0.0 --port 8000`

### Option 2: Deploy on Railway

```bash
# Install Railway CLI
npm i -g @railway/cli

# Login
railway login

# Initialize project
railway init

# Deploy
railway up
```

## Frontend Deployment

### Web (Firebase Hosting)

```bash
cd frontend

# Build web
flutter build web

# Install Firebase CLI
npm install -g firebase-tools

# Login
firebase login

# Deploy
firebase deploy
```

### Android (Google Play Store)

```bash
cd frontend/android

# Create keystore
keytool -genkey -v -keystore ~/upload-keystore.jks -keyalg RSA -keysize 2048 -validity 10000 -alias upload

# Configure Gradle
# Edit android/app/build.gradle with signing config

# Build APK
flutter build apk --release

# Build AAB (for Play Store)
flutter build appbundle --release
```

### iOS (App Store)

```bash
cd frontend/ios

# Create certificates in Apple Developer Console

# Build iOS
flutter build ios --release

# Archive and upload to App Store via Xcode
```

## Firebase Setup

### Firestore Database

1. Create database in Firebase Console
2. Deploy security rules:
   ```bash
   firebase deploy --only firestore:rules
   ```

### Firebase Storage

1. Create storage bucket
2. Deploy storage rules:
   ```bash
   firebase deploy --only storage
   ```

### Firebase Authentication

Enable:
- Email/Password authentication
- Google Sign-in
- Email verification

## Database Configuration

### MongoDB Atlas (Optional)

1. Create cluster on MongoDB Atlas
2. Get connection string
3. Add to .env: `MONGODB_URL=<connection-string>`

## Environment Variables

Create `.env` file with:

```
DEBUG=False
SECRET_KEY=your-super-secret-key
FIREBASE_CREDENTIALS=/path/to/service-account.json
OPENAI_API_KEY=sk-...
MONGODB_URL=mongodb+srv://...
```

## Monitoring

- **Backend**: Use Render/Railway monitoring dashboard
- **Frontend**: Firebase Analytics
- **Errors**: Set up Sentry for error tracking

## SSL Certificate

- Automatic for Render and Railway
- Firebase Hosting provides automatic SSL

## CDN

- Firebase Hosting uses Google CDN
- Consider Cloudflare for additional caching

## Health Checks

Monitor these endpoints:
- `/health` - Backend health
- `/api/auth/verify-token` - Auth system
- Firebase Realtime Database connection

## Scaling

- Backend: Increase dyno/railway resources
- Database: Enable Firestore auto-scaling
- Storage: Enable versioning and lifecycle rules
- CDN: Adjust caching headers
