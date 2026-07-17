#!/bin/bash
# CampusVault Project Setup Script

echo "🚀 CampusVault Setup"
echo "===================="
echo ""

# Check prerequisites
echo "Checking prerequisites..."

# Check Flutter
if ! command -v flutter &> /dev/null; then
    echo "❌ Flutter not installed. Please install Flutter from https://flutter.dev"
    exit 1
fi

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python not installed. Please install Python 3.8+"
    exit 1
fi

echo "✅ Prerequisites check passed"
echo ""

# Setup Backend
echo "Setting up backend..."
cd backend

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" ]]; then
    source venv/Scripts/activate
else
    source venv/bin/activate
fi

# Install dependencies
pip install -r requirements.txt

# Copy .env file
if [ ! -f .env ]; then
    cp .env.example .env
    echo "⚠️  Created .env file - Please update with your credentials"
fi

cd ..
echo "✅ Backend setup complete"
echo ""

# Setup Frontend
echo "Setting up frontend..."
cd frontend

# Get Flutter dependencies
flutter pub get

# Generate code
flutter pub run build_runner build --delete-conflicting-outputs

cd ..
echo "✅ Frontend setup complete"
echo ""

echo "🎉 Setup complete!"
echo ""
echo "Next steps:"
echo "1. Backend:"
echo "   - Update backend/.env with Firebase credentials"
echo "   - Run: cd backend && source venv/bin/activate && python -m uvicorn app.main:app --reload"
echo ""
echo "2. Frontend:"
echo "   - Update Firebase credentials in lib/firebase_options.dart"
echo "   - Run: flutter run"
echo ""
