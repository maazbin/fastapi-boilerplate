"""
FastAPI dependencies for route protection.
"""
from fastapi import Request, Header
from app.session import extract_token, get_session
from app.core.exceptions import NotAuthenticated, SessionExpired
from typing import Dict, Any


async def validate_session(
    request: Request,
    authorization: str = Header(..., description="Bearer <jwt_token>")
) -> Dict[str, Any]:
    """
    Validates session and returns user data.
    
    Returns:
        User data dict with user_id, email, is_active
        
    Raises:
        NotAuthenticated: No token or invalid format
        SessionExpired: Token expired
    """
    token = extract_token(authorization)
    if not token:
        raise NotAuthenticated()
    
    user = get_session(token)
    if not user:
        raise SessionExpired()
    
    request.state.session["user"] = user
    request.state.session["token"] = token
    
    return user


def get_current_token(request: Request) -> str:
    """Get current token from request.state.session."""
    token = request.state.session.get("token")
    if not token:
        raise NotAuthenticated()
    return token
