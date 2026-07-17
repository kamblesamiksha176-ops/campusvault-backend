# CampusVault Platform Setup Guide

## 🤖 Android Setup

### Prerequisites
- Android Studio installed
- Android SDK 21+ (API level)
- Gradle

### Configuration

1. **Update Gradle Version** (if needed)
   - Edit `android/build.gradle`
   - Set `minSdkVersion = 21`
   - Set `targetSdkVersion = 34`

2. **Add Google Services**
   ```bash
   # Download google-services.json from Firebase Console
   # Place it in: android/app/google-services.json
   ```

3. **Configure Permissions**
   - File: `android/app/src/main/AndroidManifest.xml`
   - Permissions for camera, storage, microphone are auto-added by packages

4. **Enable MultiDex** (if APK gets large)
   - Edit `android/app/build.gradle`
   - Add: `multiDexEnabled = true`

### Build & Run

```bash
# Run on connected device
flutter run

# Build APK (debug)
flutter build apk --debug

# Build APK (release)
flutter build apk --release

# Build App Bundle (for Play Store)
flutter build appbundle --release
```

---

## 🍎 iOS Setup

### Prerequisites
- macOS with Xcode
- CocoaPods
- iOS 11.0+

### Configuration

1. **Update iOS Deployment Target**
   ```bash
   # Edit ios/Podfile
   platform :ios, '11.0'
   ```

2. **Add Google Services**
   - Download GoogleService-Info.plist from Firebase
   - Open `ios/Runner.xcworkspace` in Xcode
   - Add file via Xcode (not Finder)

3. **Enable Capabilities**
   - Open `ios/Runner.xcworkspace` in Xcode
   - Select Runner project
   - Select Runner target
   - Capabilities tab:
     - Enable Push Notifications
     - Enable Sign In with Apple (if needed)

4. **Update Info.plist**
   ```xml
   <!-- ios/Runner/Info.plist -->
   <key>NSPhotoLibraryUsageDescription</key>
   <string>We need access to your photos</string>
   <key>NSCameraUsageDescription</key>
   <string>We need access to your camera</string>
   <key>NSMicrophoneUsageDescription</key>
   <string>We need access to your microphone</string>
   ```

### Build & Run

```bash
# Run on connected device
flutter run

# Build for iOS
flutter build ios --release

# Create IPA (for distribution)
flutter build ipa --release
```

---

## 🌐 Web Setup

### Configuration

1. **No additional setup needed** - Web build is ready
2. **Supported browsers**:
   - Chrome
   - Firefox
   - Safari
   - Edge

### Build & Run

```bash
# Enable web (one time)
flutter config --enable-web

# Run on web
flutter run -d web

# Build for web
flutter build web --release

# Output: build/web/
```

### Deployment

```bash
# Deploy to Firebase Hosting
firebase deploy --only hosting

# Or deploy to your own web server
# Copy build/web/* to your server
```

---

## 💻 Windows Setup

### Prerequisites
- Visual Studio with C++ build tools
- Windows 10/11

### Configuration

1. **No special configuration needed**

### Build & Run

```bash
# Run on Windows
flutter run -d windows

# Build for Windows
flutter build windows

# Output: build/windows/runner/Release/campusvault.exe
```

---

## 🐧 Linux Setup

### Prerequisites
- Ubuntu/Debian with development tools
- CMake, Ninja, pkg-config

### Configuration

```bash
# Install dependencies (Ubuntu/Debian)
sudo apt-get install -y \
  clang cmake git ninja-build pkg-config \
  libgtk-3-dev liblzma-dev libstdc++-12-dev

# For other Linux distributions, see:
# https://flutter.dev/docs/get-started/install/linux
```

### Build & Run

```bash
# Run on Linux
flutter run -d linux

# Build for Linux
flutter build linux

# Output: build/linux/x64/release/bundle/
```

---

## 📦 Firebase SDK Setup

### Step 1: Create Firebase Project

1. Go to [firebase.google.com](https://firebase.google.com)
2. Click "Add Project"
3. Name: "CampusVault"
4. Enable Google Analytics
5. Create project

### Step 2: Add Android App

1. Project Settings → Add App → Android
2. Package Name: `com.graminpoint.campusvault`
3. Download `google-services.json`
4. Place in `android/app/`

### Step 3: Add iOS App

1. Project Settings → Add App → iOS
2. Bundle ID: `com.graminpoint.campusvault`
3. Download `GoogleService-Info.plist`
4. Add to Xcode project

### Step 4: Add Web App

1. Project Settings → Add App → Web
2. Copy Firebase config
3. Update `lib/firebase_options.dart`

### Step 5: Configure Services

#### Enable Authentication
1. Build → Authentication
2. Sign-in providers:
   - Email/Password ✅
   - Google ✅

#### Create Firestore Database
1. Build → Firestore Database
2. Start in test mode (development)
3. Location: `us-central1`

#### Setup Storage
1. Build → Storage
2. Create bucket
3. Location: `us-central1`

---

## 🔗 Deep Linking Setup (Optional)

### Android
```xml
<!-- android/app/src/main/AndroidManifest.xml -->
<activity android:name=".MainActivity">
  <intent-filter>
    <action android:name="android.intent.action.VIEW" />
    <category android:name="android.intent.category.DEFAULT" />
    <category android:name="android.intent.category.BROWSABLE" />
    <data android:scheme="campusvault" android:host="campusvault.com" />
  </intent-filter>
</activity>
```

### iOS
```xml
<!-- ios/Runner/Info.plist -->
<key>CFBundleURLTypes</key>
<array>
  <dict>
    <key>CFBundleTypeRole</key>
    <string>Editor</string>
    <key>CFBundleURLSchemes</key>
    <array>
      <string>campusvault</string>
    </array>
  </dict>
</array>
```

---

## 🧪 Testing on Different Platforms

### Android Emulator
```bash
# Start emulator
flutter emulators --launch <emulator_name>

# List available emulators
flutter emulators
```

### iOS Simulator
```bash
# Start simulator
open -a Simulator

# List simulators
xcrun simctl list
```

### Web Browser DevTools
```bash
# Run with DevTools
flutter run -d web --debug

# Then press 'd' for DevTools
```

---

## ⚙️ Advanced Configuration

### Enable Null Safety
Already enabled! Uses `sdk: '>=3.2.0 <4.0.0'`

### Enable Web Plugins
Already included in dependencies

### Internationalization
Already included `intl` package

### Localization
Ready to add language translations to `lib/l10n/`

---

## 🐛 Common Platform Issues

### Android: Build fails
```bash
flutter clean
flutter pub get
flutter build apk
```

### iOS: Pod issues
```bash
cd ios
rm Podfile.lock
pod install
cd ..
flutter run
```

### Web: CORS errors
- Handled in backend with CORS middleware
- Update CORS_ORIGINS in backend/.env

---

## 📊 Platform Support Matrix

| Feature | Android | iOS | Web | Windows | Linux |
|---------|---------|-----|-----|---------|-------|
| Firebase Auth | ✅ | ✅ | ✅ | ✅ | ⚠️ |
| Firestore | ✅ | ✅ | ✅ | ✅ | ⚠️ |
| Storage | ✅ | ✅ | ✅ | ✅ | ⚠️ |
| Image Picker | ✅ | ✅ | ✅ | ✅ | ✅ |
| Video Player | ✅ | ✅ | ✅ | ✅ | ✅ |
| Downloads | ✅ | ✅ | ✅ | ✅ | ⚠️ |

---

## 🚀 Performance Optimization

### Android
- Use release builds for testing
- Enable ProGuard/R8 minification
- Test on actual devices

### iOS
- Use release builds
- Test on different iOS versions
- Monitor memory usage

### Web
- Enable compression
- Use lazy loading
- Optimize bundle size

---

## 📋 Checklist Before Release

- [ ] All platforms tested
- [ ] Firebase properly configured
- [ ] Environment variables set
- [ ] API endpoints working
- [ ] Firebase Realtime Database rules set
- [ ] Storage rules configured
- [ ] Authentication working
- [ ] All features tested
- [ ] No console errors
- [ ] Performance acceptable
- [ ] App icons added
- [ ] Splash screens added

---

For more information, see official documentation:
- [Flutter Docs](https://flutter.dev/docs)
- [Firebase Docs](https://firebase.google.com/docs)
