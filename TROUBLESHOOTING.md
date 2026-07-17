# CampusVault Troubleshooting Guide

## 🔧 Common Issues & Solutions

---

## Flutter Issues

### Issue: `flutter pub get` fails with version conflicts

**Error:**
```
Because campusvault depends on permission_handler ^11.4.4 which doesn't match 
any versions available...
```

**Solution:**
1. Update `pubspec.yaml` with compatible versions
2. Run: `flutter clean`
3. Run: `flutter pub get`
4. If still fails: `flutter pub upgrade`

**Files updated:**
- ✅ `pubspec.yaml` - Dependencies corrected

---

### Issue: "No supported devices connected"

**Error:**
```
No supported devices connected.
```

**Solutions:**
1. **Android:**
   ```bash
   # List emulators
   flutter emulators
   
   # Start emulator
   flutter emulators --launch <emulator_name>
   
   # Or connect a device via USB
   flutter devices
   ```

2. **iOS:**
   ```bash
   # List simulators
   xcrun simctl list
   
   # Start simulator
   open -a Simulator
   
   # Or connect a device
   flutter devices
   ```

3. **Web:**
   ```bash
   flutter run -d web
   ```

---

### Issue: "Hot reload not working"

**Solutions:**
1. Use hot restart instead: `R` key
2. Try full restart: `flutter run`
3. Check for compilation errors in terminal
4. Rebuild: `flutter clean && flutter run`

---

### Issue: "Build Gradle failure on Android"

**Error:**
```
FAILURE: Build failed with an exception.
```

**Solutions:**
```bash
# Clean and rebuild
flutter clean
rm -rf android/.gradle
flutter pub get
flutter run

# Or update Gradle
cd android
./gradlew wrapper --gradle-version 8.0
cd ..
flutter run
```

---

### Issue: "CocoaPods error on iOS"

**Error:**
```
Error running pod install
```

**Solutions:**
```bash
# Clean and reinstall
cd ios
rm -rf Pods
rm Podfile.lock
pod deintegrate
pod install
cd ..
flutter run

# Or update CocoaPods
sudo gem install cocoapods
pod repo update
```

---

### Issue: "Firebase initialization fails"

**Error:**
```
Firebase initialization failed
```

**Solutions:**
1. **Update firebase_options.dart:**
   ```dart
   // Copy your Firebase config from Console
   static const FirebaseOptions web = FirebaseOptions(
     apiKey: 'YOUR_API_KEY',
     appId: 'YOUR_APP_ID',
     messagingSenderId: 'YOUR_MESSAGING_SENDER_ID',
     projectId: 'your-project-id',
     authDomain: 'your-project-id.firebaseapp.com',
     storageBucket: 'your-project-id.appspot.com',
   );
   ```

2. **Check Android google-services.json:**
   ```bash
   # Should be at android/app/google-services.json
   ls -la android/app/google-services.json
   ```

3. **Check iOS GoogleService-Info.plist:**
   ```bash
   # Should be added to Xcode project
   # ios/Runner/GoogleService-Info.plist
   ```

---

### Issue: "Model import errors - can't find generated files"

**Error:**
```
The method 'fromJson' isn't defined for the class 'User'.
```

**Solutions:**
```bash
# Generate code
flutter pub run build_runner build --delete-conflicting-outputs

# Or force regenerate
flutter pub run build_runner build --delete-conflicting-outputs --verbose
```

---

## Python/Backend Issues

### Issue: "ModuleNotFoundError" when starting backend

**Error:**
```
ModuleNotFoundError: No module named 'fastapi'
```

**Solutions:**
```bash
# Make sure venv is activated
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate

# Then install requirements
pip install -r requirements.txt

# Verify installation
python -m pip list | grep fastapi
```

---

### Issue: "Port 8000 already in use"

**Error:**
```
OSError: [Errno 48] Address already in use
```

**Solutions:**
```bash
# Use different port
python -m uvicorn app.main:app --port 8001

# Or kill process using port
# Windows
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# Linux/Mac
lsof -ti:8000 | xargs kill -9
```

---

### Issue: "Firebase credentials file not found"

**Error:**
```
FileNotFoundError: [Errno 2] No such file or directory: 'firebase_credentials.json'
```

**Solutions:**
1. Download service account key from Firebase Console
2. Place in `backend/` directory
3. Update `.env`:
   ```
   FIREBASE_CREDENTIALS=firebase_credentials.json
   ```

---

### Issue: "OpenAI API key invalid"

**Error:**
```
AuthenticationError: Incorrect API key provided
```

**Solutions:**
1. Check API key in `.env`
2. Make sure it starts with `sk-`
3. Verify key has API access enabled
4. Update in Firebase for AI features

---

### Issue: "Pydantic validation error"

**Error:**
```
validation error for UserCreate
```

**Solutions:**
1. Check request body matches model
2. Use `/docs` to test endpoints
3. Verify all required fields present
4. Check email format for EmailStr

---

## Firebase Issues

### Issue: "Firestore permission denied"

**Error:**
```
Permission denied: missing or insufficient permissions
```

**Solutions:**
1. Deploy Firestore rules:
   ```bash
   firebase deploy --only firestore:rules
   ```

2. Or enable test mode temporarily:
   - Firebase Console → Firestore → Rules
   - Switch to test mode
   - Then configure proper rules

3. Check rules file: [firestore.rules](firestore.rules)

---

### Issue: "Storage upload fails"

**Error:**
```
Permission denied: Firebase Storage permission denied
```

**Solutions:**
1. Deploy storage rules:
   ```bash
   firebase deploy --only storage
   ```

2. Or enable test mode temporarily

3. Check rules file: [storage.rules](storage.rules)

---

### Issue: "Authentication error"

**Error:**
```
PERMISSION_DENIED: Missing or insufficient permissions
```

**Solutions:**
1. Enable authentication method in Firebase Console
2. Verify email/password is enabled
3. Verify Google sign-in is configured
4. Check authentication rules

---

## Database Issues

### Issue: "Firestore queries not working"

**Solutions:**
1. Check collection name spelling
2. Verify document structure matches model
3. Create indexes if needed
4. Check Firestore rules allow read access
5. Verify authentication token valid

---

### Issue: "Firestore rules blocking access"

**Error:**
```
Missing or insufficient permissions
```

**Solutions:**
1. Review `firestore.rules`
2. Add debug logging to rules
3. Test with simpler rules first
4. Check user role assignments
5. Verify subscription field exists

---

## API Issues

### Issue: "API endpoint returns 404"

**Error:**
```
404 Not Found: No route matches the given path
```

**Solutions:**
1. Check endpoint path matches routes
2. Verify app.include_router() called
3. Check URL has /api prefix
4. Verify request method (GET/POST/etc)
5. Check route parameters

---

### Issue: "CORS error in frontend"

**Error:**
```
Access to XMLHttpRequest blocked by CORS policy
```

**Solutions:**
1. Check CORS middleware in backend
2. Update CORS_ORIGINS in config.py:
   ```python
   CORS_ORIGINS = ["*"]  # for dev
   # Or specific origins for prod
   CORS_ORIGINS = ["https://yourdomain.com"]
   ```
3. Restart backend server

---

### Issue: "Slow API responses"

**Solutions:**
1. Add pagination to large queries
2. Add database indexes
3. Use caching
4. Optimize database queries
5. Monitor with monitoring tools

---

## Network Issues

### Issue: "Cannot connect to backend from frontend"

**Error:**
```
Connection refused or timeout
```

**Solutions:**
1. **Verify backend is running:**
   ```bash
   curl http://localhost:8000/
   ```

2. **Check IP address:**
   ```bash
   # Use machine IP, not localhost for Android
   # In AI service: use 192.168.x.x:8000
   ```

3. **Check firewall:**
   ```bash
   # Windows
   netsh advfirewall firewall add rule name="CampusVault" dir=in action=allow protocol=tcp localport=8000
   ```

4. **Verify URL in services:**
   ```dart
   final String _baseUrl = 'http://10.0.2.2:8000/api'; // Android emulator
   final String _baseUrl = 'http://127.0.0.1:8000/api'; // iOS simulator
   final String _baseUrl = 'http://localhost:8000/api'; // Web
   ```

---

## Platform-Specific Issues

### Android Issues

#### Issue: "android/app/google-services.json not found"
```bash
# Download from Firebase Console
# Place at: android/app/google-services.json
```

#### Issue: "minSdkVersion too low"
```gradle
// android/app/build.gradle
android {
    compileSdkVersion 34
    minSdkVersion 21
    targetSdkVersion 34
}
```

### iOS Issues

#### Issue: "iOS deployment target mismatch"
```
error: The iOS deployment target 'IPHONEOS_DEPLOYMENT_TARGET' is set to 9.0, but the range of supported deployment target versions is 11.0 to 14.5.
```

Solution:
```ruby
# ios/Podfile
platform :ios, '11.0'
```

#### Issue: "Xcode build failure"
```bash
cd ios
pod install
cd ..
flutter clean
flutter run
```

### Web Issues

#### Issue: "App not loading on web"
```bash
# Enable web support
flutter config --enable-web

# Run with verbose output
flutter run -d web --verbose
```

#### Issue: "Firebase not working on web"
Ensure `lib/firebase_options.dart` has web config:
```dart
static const FirebaseOptions web = FirebaseOptions(
  // ... web specific config
);
```

---

## Performance Issues

### Issue: "App is slow"

**Solutions:**
1. Profile with DevTools:
   ```bash
   flutter run --profile
   # Press 'p' to enable performance overlay
   ```

2. Optimize images (reduce resolution)
3. Use lazy loading for lists
4. Enable Firestore caching
5. Reduce API call frequency
6. Use pagination

### Issue: "High memory usage"

**Solutions:**
1. Dispose controllers properly
2. Clear image cache
3. Limit list view rendering
4. Use `.maybeMap()` carefully
5. Monitor with DevTools Memory tab

---

## Debugging Tips

### Enable Verbose Logging

```bash
flutter run -v
```

### View Firebase Logs

```bash
firebase functions:log
```

### Use FastAPI Interactive Docs

```
http://localhost:8000/docs
```

### Android Studio Logcat

```bash
flutter logs
```

### iOS Console

```bash
xcrun simctl spawn booted log stream --predicate 'process == "Runner"'
```

---

## Getting Help

1. **Check Logs:** Full error messages in terminal
2. **Read Documentation:** See provided markdown files
3. **API Documentation:** `/docs` endpoint
4. **Firebase Console:** Check database and rules
5. **Stack Overflow:** Search error message
6. **Official Docs:**
   - Flutter: https://flutter.dev/docs
   - FastAPI: https://fastapi.tiangolo.com
   - Firebase: https://firebase.google.com/docs

---

## Common Commands Reference

```bash
# Flutter
flutter clean                    # Clean build files
flutter pub get                 # Get dependencies
flutter pub upgrade             # Upgrade dependencies
flutter run                     # Run app
flutter build apk              # Build Android APK
flutter build ios              # Build iOS app
flutter build web              # Build web app

# Backend
python -m venv venv            # Create venv
source venv/bin/activate       # Activate (Linux/Mac)
pip install -r requirements.txt # Install deps
python -m uvicorn app.main:app --reload  # Run server

# Firebase
firebase login                  # Login to Firebase
firebase deploy                 # Deploy rules
firebase functions:log          # View logs
```

---

## Still Stuck?

1. Review error message carefully
2. Check documentation in this repo
3. Check terminal output for hints
4. Try similar issues on Stack Overflow
5. Review official framework docs
6. Ask in community forums

---

**Don't give up! The solution is usually in the error message. 🔍**
