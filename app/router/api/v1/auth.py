"""
Authentication router - login/logout/register.
"""
from typing import Dict, Any
from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.dependencies import validate_session, get_current_token
from app.service.auth_service import AuthService
from app.schema.auth import UserRegister, UserLogin, LoginResponse, MessageResponse
import logging

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/register", response_model=MessageResponse)
async def register(
    user_data: UserRegister,
    db: Session = Depends(get_db)
):
    """Register a new user."""
    auth_service = AuthService(db)
    auth_service.register_user(user_data)
    return MessageResponse(message="User registered successfully")


@router.post("/login", response_model=LoginResponse)
async def login(
    login_data: UserLogin,
    db: Session = Depends(get_db)
):
    """Login and get JWT token."""
    auth_service = AuthService(db)
    return auth_service.login(login_data)


@router.post("/logout", response_model=MessageResponse)
async def logout(
    request: Request,
    current_user: Dict[str, Any] = Depends(validate_session),
    db: Session = Depends(get_db)
):
    """Logout - invalidates token server-side."""
    auth_service = AuthService(db)
    token = get_current_token(request)
    auth_service.logout(token)
    logger.info(f"User logged out: {current_user['email']}")
    return MessageResponse(message="Logged out successfully")
