"""
User router - profile endpoints (protected).
"""
from typing import Dict, Any
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.dependencies import validate_session
from app.service.user_service import UserService
from app.schema.auth import UserProfile

router = APIRouter()


@router.get("/me", response_model=UserProfile)
async def get_me(
    current_user: Dict[str, Any] = Depends(validate_session),
    db: Session = Depends(get_db)
):
    """Get current user profile."""
    user_service = UserService(db)
    return user_service.get_profile(current_user["user_id"])
