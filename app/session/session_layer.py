"""
Session layer - in-memory token store and validation.
In production, use Redis for multi-instance support.
"""
from typing import Optional, Dict, Any
from app.core.security import verify_access_token
import logging

logger = logging.getLogger(__name__)

# In-memory session store: {token: user_data}
_sessions: Dict[str, Dict[str, Any]] = {}


def create_session(token: str, user_data: Dict[str, Any]) -> None:
    """Store token and user data in session."""
    _sessions[token] = user_data
    logger.info(f"Session created for user: {user_data.get('email')}")


def get_session(token: str) -> Optional[Dict[str, Any]]:
    """Get user data from session if token exists and JWT is valid."""
    if token not in _sessions:
        return None
    
    payload = verify_access_token(token)
    if not payload:
        remove_session(token)
        return None
    
    return _sessions[token]


def remove_session(token: str) -> bool:
    """Remove token from session (logout)."""
    if token in _sessions:
        user_data = _sessions.pop(token)
        logger.info(f"Session removed for user: {user_data.get('email')}")
        return True
    return False


def is_valid_session(token: str) -> bool:
    """Check if token has valid session."""
    return get_session(token) is not None


def extract_token(auth_header: Optional[str]) -> Optional[str]:
    """Extract JWT token from Authorization header."""
    if not auth_header:
        return None
    
    parts = auth_header.split(" ")
    if len(parts) != 2 or parts[0].lower() != "bearer":
        return None
    
    return parts[1]
