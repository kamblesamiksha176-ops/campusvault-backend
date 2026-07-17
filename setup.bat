@echo off
REM CampusVault Project Setup Script for Windows

echo 🚀 CampusVault Setup
echo ====================
echo.

REM Check Flutter
where flutter >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo ❌ Flutter not installed. Please install Flutter from https://flutter.dev
    exit /b 1
)

REM Check Python
where python >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo ❌ Python not installed. Please install Python 3.8+
    exit /b 1
)

echo ✅ Prerequisites check passed
echo.

REM Setup Backend
echo Setting up backend...
cd backend

REM Create virtual environment
python -m venv venv

REM Activate virtual environment
call venv\Scripts\activate

REM Install dependencies
pip install -r requirements.txt

REM Copy .env file
if not exist .env (
    copy .env.example .env
    echo ⚠️  Created .env file - Please update with your credentials
)

cd ..
echo ✅ Backend setup complete
echo.

REM Setup Frontend
echo Setting up frontend...
cd frontend

REM Get Flutter dependencies
call flutter pub get

REM Generate code
call flutter pub run build_runner build --delete-conflicting-outputs

cd ..
echo ✅ Frontend setup complete
echo.

echo 🎉 Setup complete!
echo.
echo Next steps:
echo 1. Backend:
echo    - Update backend\.env with Firebase credentials
echo    - Run: cd backend ^&^& venv\Scripts\activate ^&^& python -m uvicorn app.main:app --reload
echo.
echo 2. Frontend:
echo    - Update Firebase credentials in lib/firebase_options.dart
echo    - Run: flutter run
echo.

pause
