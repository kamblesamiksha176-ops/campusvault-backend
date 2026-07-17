# CampusVault - AI Powered Smart Learning Platform

A comprehensive educational platform built with Flutter, FastAPI, and Firebase.

## 📁 Project Structure

```
campusvault/
├── frontend/                    # Flutter Mobile & Web App
│   ├── lib/
│   │   ├── main.dart           # App entry point
│   │   ├── models/             # Data models
│   │   │   ├── user_model.dart
│   │   │   ├── resource_model.dart
│   │   │   ├── quiz_model.dart
│   │   │   ├── subscription_model.dart
│   │   │   └── notification_model.dart
│   │   ├── services/           # API & Firebase services
│   │   │   ├── auth_service.dart
│   │   │   ├── resource_service.dart
│   │   │   └── ai_service.dart
│   │   ├── screens/            # UI Screens by role
│   │   │   ├── auth/
│   │   │   ├── student/
│   │   │   ├── teacher/
│   │   │   └── admin/
│   │   ├── widgets/            # Reusable widgets
│   │   ├── theme/              # App theme & colors
│   │   ├── utils/              # Utilities & constants
│   │   └── constants/
│   ├── pubspec.yaml            # Flutter dependencies
│   ├── android/                # Android configuration
│   ├── ios/                    # iOS configuration
│   └── web/                    # Web platform
│
├── backend/                    # FastAPI Backend
│   ├── app/
│   │   ├── main.py            # FastAPI app initialization
│   │   ├── config.py          # Configuration settings
│   │   ├── models.py          # Pydantic models
│   │   ├── routes/            # API endpoints
│   │   │   ├── auth.py        # Authentication endpoints
│   │   │   ├── resources.py   # Resource management
│   │   │   ├── ai.py          # AI features
│   │   │   ├── admin.py       # Admin dashboard
│   │   │   └── __init__.py
│   │   └── __init__.py
│   ├── requirements.txt        # Python dependencies
│   └── .env.example           # Environment template
│
└── firebase-config.json.example  # Firebase setup template

```

## 🚀 Quick Start

### Frontend Setup

```bash
# Navigate to frontend
cd frontend

# Get Flutter dependencies
flutter pub get

# Generate code (for JSON serialization)
flutter pub run build_runner build

# Run on device
flutter run

# Run on web
flutter run -d web
```

### Backend Setup

```bash
# Navigate to backend
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
cp .env.example .env

# Run server
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Firebase Setup

1. Create a Firebase project at [Firebase Console](https://console.firebase.google.com/)
2. Enable Firebase services:
   - Authentication (Email, Google Sign-in)
   - Cloud Firestore
   - Cloud Storage
   - Realtime Database
3. Download service account key and save as `firebase_credentials.json` in backend
4. Add Firebase config to Flutter app (android/app/google-services.json)

## 📋 Features

### Student Features
- 📚 View and download study materials
- 🎥 Watch video lectures
- 📝 Take quizzes and mock tests
- 🤖 Chat with AI tutor
- 🔖 Bookmark favorite resources
- 💾 Offline download support
- 📊 Leaderboard rankings
- 🔔 Notifications for new content

### Teacher Features
- 📤 Upload notes, PDFs, PPTs
- 🎬 Upload video lectures
- 📋 Create assignments
- ❓ Upload question papers
- 📢 Post announcements
- 📊 View upload statistics

### Admin Features
- 👥 Manage users (activate/deactivate)
- 📦 Manage resources
- 💳 Manage subscriptions
- 📊 View platform analytics
- ⚙️ Configure AI settings
- 🔐 Manage user roles

### AI Features
- 💬 AI tutor chat
- 📝 Quiz generation
- 📄 Document summarization
- 🛣️ Learning roadmap generation
- 💼 Career guidance
- 🔧 Code debugging help

## 🎨 Design System

- **Theme**: Dark Mode (Material 3)
- **Primary Color**: #2563EB (Blue)
- **Accent Color**: #22D3EE (Cyan)
- **Premium Color**: #F59E0B (Amber)
- **Success Color**: #10B981 (Green)
- **Card Background**: #162544

## 🔐 Authentication Flow

```
Splash Screen
    ↓
Role Selection (Student/Teacher/Admin)
    ↓
Login/Register
    ↓
Email Verification
    ↓
Read User Role from Firestore
    ↓
Dashboard (Role-specific)
```

## 📦 API Endpoints

### Authentication
- `POST /api/auth/register` - Register new user
- `POST /api/auth/login` - Login
- `POST /api/auth/forgot-password` - Password reset
- `POST /api/auth/verify-token` - Verify JWT token

### Resources
- `GET /api/resources/all` - Get all resources
- `GET /api/resources/search` - Search resources
- `POST /api/resources/upload` - Upload resource
- `DELETE /api/resources/{id}` - Delete resource

### AI
- `POST /api/ai/chat` - Chat with AI
- `POST /api/ai/generate-quiz` - Generate quiz
- `POST /api/ai/explain` - Explain topic
- `POST /api/ai/summarize` - Summarize content

### Admin
- `GET /api/admin/users` - Get all users
- `DELETE /api/admin/users/{id}` - Delete user
- `GET /api/admin/analytics` - Get analytics

## 🗄️ Database Schema

### Users Collection
```
{
  uid: string
  name: string
  email: string
  phone: string
  college: string
  branch: string
  semester: number
  role: "student" | "teacher" | "admin"
  subscription: boolean
  emailVerified: boolean
  createdAt: timestamp
}
```

### Resources Collection
```
{
  documentId: string
  title: string
  description: string
  subject: string
  branch: string
  semester: number
  type: "notes" | "ppt" | "video" | "assignment" | "questionPaper"
  fileUrl: string
  uploadedBy: string
  premium: boolean
  downloads: number
  views: number
  createdAt: timestamp
}
```

## 🚢 Deployment

### Frontend
- Flutter Web: Firebase Hosting
- Android APK: Google Play Store
- iOS: Apple App Store

### Backend
- FastAPI: Render, Railway, or DigitalOcean
- Database: Firebase Firestore
- Storage: Firebase Storage

## 📝 Development Notes

- All models support JSON serialization
- Services follow singleton pattern
- UI uses Material 3 design guidelines
- Theme colors are centralized in `app_theme.dart`
- Riverpod for state management
- Firebase rules must be configured for security

## 🔄 Update Models

After modifying models:
```bash
cd frontend
flutter pub run build_runner build --delete-conflicting-outputs
```

## 📚 Documentation

Detailed documentation coming soon for:
- Advanced features setup
- Cloud function examples
- Firestore security rules
- CI/CD pipeline
- Testing guidelines

## 📄 License

MIT License - See LICENSE file for details

## 👥 Support

For support, email: support@campusvault.com

---

**Built with ❤️ for students**
