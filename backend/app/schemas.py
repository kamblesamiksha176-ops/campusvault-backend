"""
CampusVault - Database Models
Pydantic models for data validation and serialization
"""

from typing import Optional, List
from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserBase(BaseModel):
    name: str
    email: EmailStr
    phone: Optional[str] = None
    college: Optional[str] = None
    branch: Optional[str] = None
    semester: Optional[int] = None

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    uid: str
    role: str
    subscription: bool
    emailVerified: bool
    createdAt: datetime

    class Config:
        from_attributes = True

class ResourceBase(BaseModel):
    title: str
    description: str
    subject: str
    branch: str
    semester: int

class ResourceCreate(ResourceBase):
    type: str
    premium: bool = False

class ResourceResponse(ResourceBase):
    documentId: str
    fileUrl: str
    uploadedBy: str
    premium: bool
    downloads: int
    views: int
    createdAt: datetime

    class Config:
        from_attributes = True

class QuizBase(BaseModel):
    title: str
    subject: str
    branch: str
    semester: int

class QuizResponse(QuizBase):
    quizId: str
    createdAt: datetime

    class Config:
        from_attributes = True
