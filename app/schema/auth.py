"""
Authentication schemas.
"""
from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


class UserRegister(BaseModel):
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserInfo(BaseModel):
    id: str
    email: str
    is_active: bool


class UserProfile(UserInfo):
    """Extended user info with timestamps."""
    created_at: datetime
    updated_at: datetime


class LoginResponse(BaseModel):
    message: str
    access_token: str
    token_type: str = "bearer"
    user: UserInfo


class MessageResponse(BaseModel):
    message: str


class SessionStatus(BaseModel):
    authenticated: bool
    user: Optional[UserInfo] = None
