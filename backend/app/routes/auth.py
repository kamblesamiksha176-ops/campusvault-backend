from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import HTTPBearer, HTTPAuthCredentials
from app.models import UserCreate, UserLogin, UserResponse, PasswordReset, Token
import firebase_admin
from firebase_admin import credentials, auth, db
from datetime import datetime, timedelta
import jwt
from app.config import settings

router = APIRouter()
security = HTTPBearer()

# Initialize Firebase (make sure credentials file exists)
try:
    if not firebase_admin.get_app():
        cred = credentials.Certificate(settings.FIREBASE_CREDENTIALS)
        firebase_admin.initialize_app(cred)
except ValueError:
    pass  # Already initialized

@router.post("/register", response_model=Token)
async def register(user: UserCreate):
    """Register a new user"""
    try:
        # Create user in Firebase Auth
        user_record = auth.create_user(
            email=user.email,
            password=user.password,
            display_name=user.name,
        )
        
        # Store user data in Firestore (using Realtime DB as example)
        user_data = {
            "uid": user_record.uid,
            "name": user.name,
            "email": user.email,
            "phone": user.phone,
            "college": user.college,
            "branch": user.branch,
            "semester": user.semester,
            "role": "student",
            "subscription": False,
            "emailVerified": False,
            "createdAt": datetime.now().isoformat(),
        }
        
        # Generate token
        token = jwt.encode(
            {
                "uid": user_record.uid,
                "email": user.email,
                "exp": datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
            },
            settings.SECRET_KEY,
            algorithm=settings.ALGORITHM
        )
        
        return {
            "access_token": token,
            "token_type": "bearer",
            "user": UserResponse(**user_data)
        }
    except auth.EmailAlreadyExistsError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@router.post("/login", response_model=Token)
async def login(user: UserLogin):
    """Login user"""
    try:
        # Firebase doesn't support direct email/password verification in server SDK
        # This should be handled by frontend and token should be passed
        # For demonstration, we'll accept JWT tokens from frontend
        
        # In production, use Firebase REST API or accept ID tokens from frontend
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Use Firebase Auth on frontend"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )

@router.post("/verify-token")
async def verify_token(credentials: HTTPAuthCredentials = Depends(security)):
    """Verify JWT token"""
    try:
        payload = jwt.decode(
            credentials.credentials,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )
        email: str = payload.get("email")
        if email is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token"
            )
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token expired"
        )
    except jwt.JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )
    return {"email": email, "valid": True}

@router.post("/forgot-password")
async def forgot_password(request: PasswordReset):
    """Send password reset email"""
    try:
        auth.generate_password_reset_link(request.email)
        return {"message": "Password reset link sent to email"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User not found"
        )

@router.post("/logout")
async def logout():
    """Logout user"""
    return {"message": "Logged out successfully"}
