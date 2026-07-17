from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

# User Models
class UserCreate(BaseModel):
    name: str
    email: str
    password: str
    phone: Optional[str] = None
    college: Optional[str] = None
    branch: Optional[str] = None
    semester: Optional[int] = None

class UserLogin(BaseModel):
    email: str
    password: str

class UserResponse(BaseModel):
    uid: str
    name: str
    email: str
    role: str
    subscription: bool
    emailVerified: bool
    createdAt: datetime

class PasswordReset(BaseModel):
    email: str

class PasswordResetConfirm(BaseModel):
    token: str
    newPassword: str

# Resource Models
class ResourceCreate(BaseModel):
    title: str
    description: str
    subject: str
    branch: str
    semester: int
    type: str  # notes, ppt, video, assignment, questionPaper
    premium: bool = False

class ResourceResponse(BaseModel):
    documentId: str
    title: str
    description: str
    subject: str
    branch: str
    semester: int
    type: str
    fileUrl: str
    uploadedBy: str
    premium: bool
    downloads: int
    views: int
    createdAt: datetime

# Quiz Models
class QuestionCreate(BaseModel):
    question: str
    options: List[str]
    correctAnswer: int
    explanation: Optional[str] = None

class QuizCreate(BaseModel):
    title: str
    subject: str
    branch: str
    semester: int
    timeLimit: int
    passingPercentage: float
    questions: List[QuestionCreate]

class QuizResponse(BaseModel):
    quizId: str
    title: str
    subject: str
    branch: str
    semester: int
    createdAt: datetime

class QuizSubmit(BaseModel):
    quizId: str
    answers: List[int]

# AI Models
class ChatRequest(BaseModel):
    message: str
    context: Optional[str] = None

class ChatResponse(BaseModel):
    response: str
    timestamp: datetime

class QuizGenerateRequest(BaseModel):
    topic: str
    number_of_questions: int = 10

class ExplainRequest(BaseModel):
    topic: str

class SummarizeRequest(BaseModel):
    file_url: str

class CareerGuidanceRequest(BaseModel):
    interests: str

# Subscription Models
class SubscriptionCreate(BaseModel):
    plan: str  # monthly, quarterly, yearly
    userId: str

class SubscriptionResponse(BaseModel):
    userId: str
    plan: str
    expiryDate: Optional[datetime]
    status: str
    createdAt: datetime

# Token Models
class Token(BaseModel):
    access_token: str
    token_type: str
    user: UserResponse

class TokenData(BaseModel):
    email: Optional[str] = None
