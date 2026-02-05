"""
App security - wraps utils with app config.
"""
from typing import Optional, Dict, Any
from app.core.config import settings
from app.utils.hashing import hash_password, verify_password
from app.utils.jwt import create_token, verify_token


def get_password_hash(password: str) -> str:
    """Hash password."""
    return hash_password(password)


def check_password(plain_password: str, hashed_password: str) -> bool:
    """Verify password."""
    return verify_password(plain_password, hashed_password)


def create_access_token(data: Dict[str, Any]) -> str:
    """Create JWT access token with app config."""
    return create_token(
        data=data,
        secret_key=settings.SECRET_KEY,
        algorithm=settings.ALGORITHM,
        expires_minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )


def verify_access_token(token: str) -> Optional[Dict[str, Any]]:
    """Verify JWT access token with app config."""
    return verify_token(
        token=token,
        secret_key=settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )
