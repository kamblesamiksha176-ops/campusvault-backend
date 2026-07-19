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

# CampusVault – README.md

> **AI-Powered Educational Resource Management System**
>
> **Final Year Engineering Project**

---

# CampusVault

CampusVault is a centralized educational resource management platform designed specifically for engineering and diploma colleges. The application enables students, teachers, and administrators to collaborate through a secure cloud-based system where academic resources can be managed efficiently.

The project aims to replace the traditional method of sharing notes, assignments, question papers, and study materials through multiple platforms like WhatsApp, Telegram, Google Drive, and Email with one integrated platform.

---

# Table of Contents

* Project Overview
* Problem Statement
* Proposed Solution
* Objectives
* Technologies Used
* System Architecture
* User Roles
* Features
* Database Design
* Backend Architecture
* Frontend Architecture
* API Structure
* Authentication
* Security
* Project Workflow
* Deployment
* Current Status
* Future Scope
* Challenges Faced
* Learning Outcomes
* Conclusion

---

# Project Overview

Educational institutions generally use multiple communication platforms to distribute study materials. This makes resource management difficult for both students and teachers.

CampusVault provides one centralized platform where:

* Students can access educational resources.
* Teachers can upload learning materials.
* Administrators can manage the system.
* AI assists students in learning.

The application is built using modern web technologies following a Client–Server architecture.

---

# Problem Statement

Many educational institutions face the following challenges:

* Study materials are scattered across different platforms.
* Students spend time searching instead of learning.
* Previous year question papers are difficult to find.
* Teachers repeatedly upload the same files.
* No centralized learning platform exists.
* No AI-based academic support.
* Poor organization of educational resources.

These issues reduce productivity and create unnecessary confusion.

---

# Proposed Solution

CampusVault solves these problems by creating one secure cloud platform where:

* Teachers upload educational resources.
* Students access resources anytime.
* Authentication protects user accounts.
* AI provides educational assistance.
* Quizzes improve learning.
* Administrators monitor the platform.

The objective is to simplify educational resource management.

---

# Project Objectives

The main objectives are:

* Centralize educational resources.
* Improve accessibility.
* Reduce dependency on multiple communication platforms.
* Secure user authentication.
* Integrate Artificial Intelligence.
* Create a scalable educational platform.
* Improve collaboration between students and teachers.

---

# Technologies Used

## Frontend

* React.js
* Vite
* Tailwind CSS
* Axios
* React Router DOM
* React Icons

---

## Backend

* Python
* FastAPI
* Motor
* JWT Authentication
* Passlib (bcrypt)
* Pydantic
* REST APIs

---

## Database

* MongoDB Atlas

---

## Cloud Deployment

Frontend

* Vercel

Backend

* Render

Database

* MongoDB Atlas

---

## AI

* Gemini API (planned integration)

---

# System Architecture

```
Student / Teacher / Admin
            │
            ▼
     React Frontend
            │
            ▼
     FastAPI Backend
            │
            ▼
      MongoDB Atlas
```

The frontend sends REST API requests to the FastAPI backend.

The backend processes business logic, authentication, and communicates with MongoDB Atlas.

---

# User Roles

## Student

Students can:

* Register
* Login
* View Dashboard
* Access Resources
* Search Notes
* Download Study Materials
* Attempt Quizzes
* View Profile
* Use AI Assistant (planned)

---

## Teacher

Teachers can:

* Upload Notes
* Upload PDFs
* Upload PPTs
* Upload Assignments
* Upload Question Papers
* Create Quizzes
* Manage Resources

---

## Administrator

Administrator manages:

* Students
* Teachers
* Educational Resources
* Subjects
* Branches
* Analytics
* Premium Users (future)

---

# Features

## Authentication

* Registration
* Login
* JWT Authentication
* Password Hashing
* Protected APIs

Future:

* Email Verification
* Forgot Password
* Reset Password

---

## Dashboard

Displays:

* User Profile
* Quick Navigation
* Recent Activity
* Notifications
* Resource Statistics

---

## Resource Management

Supports:

* Notes
* PDFs
* PPTs
* Assignments
* Previous Year Question Papers

Future:

* Search
* Filter
* Download Counter
* Bookmarks

---

## Quiz Module

Supports:

* MCQ Quizzes
* Timer
* Auto Submit
* Result
* Score
* Leaderboard

---

## AI Module

Planned capabilities:

* Ask Doubts
* Explain Concepts
* Quiz Generation
* Question Bank Generation
* PDF Summarization
* Career Guidance
* Programming Help

---

## Notification Module

Future implementation:

* Teacher Upload Notification
* Quiz Notification
* Announcements

---

## Profile Module

Stores:

* Name
* Email
* Phone
* College
* Branch
* Semester
* Role

Future:

* Profile Editing
* Profile Picture
* Password Change

---

# Database Design

Collections:

```
users

resources

quizzes

quiz_attempts

bookmarks

notifications

subscriptions

chat_history

analytics
```

MongoDB Atlas stores all application data securely.

---

# Backend Architecture

The backend is developed using FastAPI.

Responsibilities include:

* Authentication
* API Development
* Database Communication
* Business Logic
* JWT Generation
* Validation
* Error Handling

Folder Structure:

```
backend/

app/

routes/

models.py

database.py

config.py

utils/

main.py
```

---

# Frontend Architecture

Developed using React.

Responsibilities:

* User Interface
* Dashboard
* Login
* Registration
* Resource Pages
* API Communication

Folder Structure:

```
frontend/

src/

components/

pages/

services/

hooks/

context/

assets/
```

---

# API Structure

Authentication APIs

```
POST /register

POST /login

GET /me
```

Resource APIs

```
GET /resources

POST /resources

DELETE /resources/{id}
```

Quiz APIs

```
POST /quiz

GET /quiz

POST /submit
```

AI APIs

```
POST /chat

POST /summarize

POST /generate-quiz
```

---

# Authentication

CampusVault uses JWT Authentication.

Workflow:

1. User registers.
2. Password is hashed.
3. Data stored in MongoDB.
4. User logs in.
5. Backend verifies credentials.
6. JWT Token generated.
7. Token used for protected APIs.

Benefits:

* Secure
* Stateless
* Scalable

---

# Security

Security measures include:

* Password Hashing
* JWT Authentication
* Protected APIs
* Input Validation
* Error Handling

Future:

* Email Verification
* Rate Limiting
* Two-Factor Authentication

---

# Project Workflow

```
User

↓

Frontend (React)

↓

FastAPI Backend

↓

MongoDB Atlas

↓

Response

↓

Frontend Dashboard
```

---

# Deployment

Frontend

Vercel

Backend

Render

Database

MongoDB Atlas

Deployment ensures the application is accessible through the internet.

---

# Current Status

### Completed

* FastAPI Backend
* MongoDB Atlas Integration
* User Registration
* User Login
* JWT Authentication
* Swagger Documentation
* React Frontend
* Deployment
* API Communication

### In Progress

* Profile Editing
* Teacher Upload Module
* Quiz Module
* AI Integration
* Notifications
* Analytics
* Premium Features

---

# Future Scope

Future enhancements include:

* AI Tutor
* Smart Resource Recommendation
* Mobile Application
* Video Lectures
* Live Classes
* Attendance Management
* Push Notifications
* Premium Learning Resources
* Performance Analytics
* Offline Mode

---

# Challenges Faced

During development the following challenges were encountered:

* Backend authentication implementation.
* MongoDB Atlas connectivity.
* JWT integration.
* Frontend–Backend communication.
* Cloud deployment.
* API testing.
* Environment variable configuration.
* Learning modern web development architecture.

These challenges provided valuable practical experience.

---

# Learning Outcomes

This project helped develop skills in:

* Full-Stack Web Development
* REST API Design
* FastAPI
* React
* MongoDB
* Authentication
* Cloud Deployment
* Debugging
* Version Control
* Software Architecture

---

# Conclusion

CampusVault is a modern educational platform that demonstrates the integration of frontend development, backend development, cloud databases, authentication, and scalable architecture.

Although some advanced modules are still under development, the project establishes a strong foundation for a centralized educational ecosystem. The modular design allows new features to be added without affecting the existing architecture.

---

## Author

**Samiksha kamble **
Diploma in computer engineering 

**Project Title:** CampusVault – AI-Powered Educational Resource Management System

---

This README is suitable for:

* ✔️ GitHub repository
* ✔️ College project submission
* ✔️ Teacher review
* ✔️ Viva preparation
* ✔️ Portfolio documentation

