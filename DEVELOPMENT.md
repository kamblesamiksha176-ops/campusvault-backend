# CampusVault Development Setup Guide

## Prerequisites

- Flutter SDK (v3.2.0 or higher)
- Python 3.8+
- Firebase Account
- Git

## Backend Setup

### 1. Set up Python Environment

```bash
cd backend

# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python -m venv venv
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment

```bash
# Copy .env.example to .env
cp .env.example .env

# Edit .env with your Firebase credentials
```

### 4. Run Development Server

```bash
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Backend will be available at: `http://localhost:8000`
API Documentation: `http://localhost:8000/docs`

## Frontend Setup

### 1. Install Flutter Dependencies

```bash
cd frontend

flutter pub get
```

### 2. Generate Code

```bash
flutter pub run build_runner build --delete-conflicting-outputs
```

### 3. Configure Firebase

- Download `google-services.json` from Firebase Console
- Place it in `frontend/android/app/`
- Update Firebase config in `lib/firebase_options.dart`

### 4. Run Application

```bash
# Android device/emulator
flutter run

# iOS device/simulator
flutter run -d iphone

# Web
flutter run -d web

# Desktop (macOS/Windows/Linux)
flutter run -d windows
```

## Firebase Setup

### Create Firestore Database

1. Go to Firebase Console
2. Create new project (or use existing)
3. Enable Firestore Database
4. Start in test mode (for development)
5. Create indexes as needed

### Enable Authentication

1. Authentication → Sign-in method
2. Enable: Email/Password, Google

### Set up Storage

1. Cloud Storage → Create bucket
2. Set location (us-central1 recommended)

## Development Workflow

### Making Changes

#### Backend
```bash
cd backend

# Make changes to files in app/

# Changes auto-reload with --reload flag
# Test endpoints at http://localhost:8000/docs
```

#### Frontend
```bash
cd frontend

# Make changes to Flutter code

# Changes auto-reload with hot-reload (R key)
# Changes requiring rebuild: use hot-restart (Shift+R)
```

### Running Tests

```bash
# Backend
cd backend
pytest

# Frontend
cd frontend
flutter test
```

## Debugging

### Backend

- Enable debug logging in config.py: `DEBUG=True`
- Check logs in terminal running uvicorn
- Use FastAPI interactive docs: `http://localhost:8000/docs`

### Frontend

- DevTools: `flutter run` then press `d`
- Logging: Add `print()` or `debugPrint()` statements
- Hot reload with state: Press `R`

## Database Testing

### Firestore Emulator (Optional)

```bash
# Install Firebase CLI
npm install -g firebase-tools

# Start emulator
firebase emulators:start --only firestore

# Update your app to use emulator
# In frontend: Update Firebase config
# In backend: Use emulator settings
```

## Adding New Features

### Adding a New Model

1. Create in `backend/app/models.py` (Pydantic)
2. Create in `frontend/lib/models/` (JSON serializable)
3. Generate Flutter code: `flutter pub run build_runner build`

### Adding a New API Endpoint

1. Create route in `backend/app/routes/`
2. Include in `backend/app/main.py`
3. Add service in `frontend/lib/services/`
4. Create UI in `frontend/lib/screens/`

### Adding a New Screen

1. Create file in `frontend/lib/screens/`
2. Add to navigation/routing
3. Update theme colors if needed
4. Test on multiple screen sizes

## Code Style

### Backend
- Follow PEP 8
- Type hints required
- Docstrings for functions

### Frontend
- Follow Dart conventions
- Use const constructors
- Document complex logic

## Commits

```bash
# Follow conventional commits
git commit -m "feat: add quiz generation feature"
git commit -m "fix: resolve Firebase auth issue"
git commit -m "docs: update setup guide"
```

## Common Issues

### Issue: Firebase credentials not found
**Solution**: Check `.env` file and ensure correct path to credentials

### Issue: Flutter build fails
**Solution**: Run `flutter clean` then `flutter pub get`

### Issue: Port 8000 already in use
**Solution**: `python -m uvicorn app.main:app --port 8001`

### Issue: Hot reload not working
**Solution**: Use hot-restart (Shift+R) or restart application

## Performance Tips

- Enable Firestore caching
- Use lazy loading for lists
- Optimize images (use appropriate sizes)
- Profile with DevTools
- Monitor API response times

## Resources

- [Flutter Documentation](https://flutter.dev/docs)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Firebase Documentation](https://firebase.google.com/docs)
- [Firestore Best Practices](https://firebase.google.com/docs/firestore/best-practices)

## Getting Help

- Check existing issues in project
- Review API documentation at `/api/docs`
- Check Firebase logs
- Review Flutter/Dart analyzer output
