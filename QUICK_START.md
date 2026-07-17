# CampusVault Quick Start Guide

## ✅ Project Ready!

Your complete CampusVault project is now set up with 54+ files across frontend and backend.

---

## 🚀 Getting Started

### Step 1: Install Backend Dependencies

```bash
cd backend

# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python -m venv venv
source venv/bin/activate

# Install packages
pip install -r requirements.txt
```

### Step 2: Configure Backend

1. Copy `.env.example` to `.env`
2. Add your Firebase credentials:
   ```
   FIREBASE_CREDENTIALS=firebase_credentials.json
   SECRET_KEY=your-secret-key
   OPENAI_API_KEY=your-openai-key
   ```

### Step 3: Start Backend Server

```bash
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

✅ Backend running at: `http://localhost:8000`
📚 API Docs at: `http://localhost:8000/docs`

---

### Step 4: Install Frontend Dependencies

```bash
cd frontend

# Clean previous builds (if any)
flutter clean

# Get dependencies
flutter pub get

# Generate code for models
flutter pub run build_runner build --delete-conflicting-outputs
```

### Step 5: Configure Firebase

1. Download `google-services.json` from Firebase Console
2. Place in `frontend/android/app/`
3. Update `lib/firebase_options.dart` with your credentials

### Step 6: Run Flutter App

```bash
# Run on Android/iOS device or emulator
flutter run

# Run on web
flutter run -d web

# Run on Windows
flutter run -d windows
```

---

## 📂 Project Structure

```
campusvault/
├── frontend/              # Flutter App
│   ├── lib/
│   │   ├── main.dart
│   │   ├── models/        # Data models
│   │   ├── services/      # API & Firebase
│   │   ├── screens/       # UI Screens
│   │   ├── widgets/       # Reusable components
│   │   ├── theme/         # Design system
│   │   └── utils/         # Helpers
│   ├── assets/            # Images, fonts, animations
│   └── pubspec.yaml       # Dependencies
│
├── backend/               # FastAPI Server
│   ├── app/
│   │   ├── main.py        # FastAPI app
│   │   ├── routes/        # API endpoints
│   │   ├── services/      # Business logic
│   │   ├── models.py      # Data models
│   │   └── config.py      # Settings
│   ├── requirements.txt   # Python packages
│   └── .env.example       # Environment template
│
└── docs/                  # Documentation
    ├── README.md
    ├── DEVELOPMENT.md
    ├── DEPLOYMENT.md
    └── API_DOCUMENTATION.md
```

---

## 🔧 Key Dependencies

### Frontend
- **Flutter**: UI framework
- **Firebase**: Auth, Database, Storage
- **Riverpod**: State management
- **Dio**: HTTP client
- **Google Fonts**: Typography

### Backend
- **FastAPI**: Web framework
- **Pydantic**: Data validation
- **Firebase-admin**: Firebase integration
- **OpenAI**: AI features

---

## ✨ Features Ready to Use

### 🎓 Student Features
- Dashboard with greeting
- Browse & download resources
- Take quizzes
- Chat with AI tutor
- Bookmark notes
- Profile management

### 👨‍🏫 Teacher Features
- Upload resources
- Manage uploaded files
- View analytics
- Post announcements

### 🛡️ Admin Features
- Manage users
- View platform analytics
- Manage subscriptions
- System settings

### 🤖 AI Features
- Chat with AI
- Generate quizzes
- Explain topics
- Summarize documents
- Learning roadmaps

---

## 🚨 Troubleshooting

### Flutter Issues

**Problem**: `flutter pub get` fails
```bash
# Solution
flutter clean
flutter pub get
```

**Problem**: Hot reload not working
```bash
# Solution
flutter run --verbose
# Or restart: Shift+R
```

### Backend Issues

**Problem**: Port 8000 already in use
```bash
# Solution
python -m uvicorn app.main:app --port 8001
```

**Problem**: Firebase credentials error
```
# Solution: Check .env file has correct path to Firebase JSON
```

---

## 📊 API Endpoints

### Auth
- `POST /api/auth/register` - Sign up
- `POST /api/auth/login` - Sign in
- `POST /api/auth/forgot-password` - Reset password

### Resources
- `GET /api/resources/all` - Get all resources
- `GET /api/resources/search` - Search resources
- `POST /api/resources/upload` - Upload resource

### AI
- `POST /api/ai/chat` - Chat with AI
- `POST /api/ai/generate-quiz` - Generate quiz
- `POST /api/ai/explain` - Explain topic

### Admin
- `GET /api/admin/users` - Get all users
- `GET /api/admin/analytics` - Get analytics

📖 Full documentation: See [API_DOCUMENTATION.md](API_DOCUMENTATION.md)

---

## 🎨 Theme Colors

```dart
Primary:   #2563EB (Blue)
Accent:    #22D3EE (Cyan)
Premium:   #F59E0B (Amber)
Success:   #10B981 (Green)
Error:     #EF4444 (Red)
Background: #050816 (Dark)
Card:      #162544 (Dark Blue)
```

---

## 📱 Supported Platforms

- ✅ Android
- ✅ iOS
- ✅ Web
- ✅ Windows
- ✅ macOS (ready)
- ✅ Linux (ready)

---

## 🔐 Security Setup

1. **Firestore Rules**: See [firestore.rules](firestore.rules)
2. **Storage Rules**: See [storage.rules](storage.rules)
3. **JWT Auth**: Backend handles token management
4. **Role-Based Access**: Student/Teacher/Admin roles

---

## 📚 Next Steps

1. **Configure Firebase**
   - Create project at firebase.google.com
   - Enable Firestore, Auth, Storage
   - Download credentials

2. **Set Environment Variables**
   - Backend: Create `.env` in backend/
   - Frontend: Update Firebase options

3. **Run Both Applications**
   - Start backend on port 8000
   - Start frontend on device/web

4. **Test Features**
   - Register as student/teacher
   - Try uploading resource
   - Test AI chat

5. **Deploy** (See DEPLOYMENT.md)
   - Backend on Render/Railway
   - Frontend on Firebase/Play Store

---

## 📞 Support

- 📖 Documentation: See `*.md` files
- 🐛 Issues: Check terminal output
- 💬 API Docs: `http://localhost:8000/docs`

---

## 🎯 Performance Tips

- Enable Firestore caching
- Use lazy loading for lists
- Compress images before uploading
- Monitor API response times
- Profile with Flutter DevTools

---

**Happy Building! 🚀**

Built with ❤️ for students and educators
