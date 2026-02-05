"""
Authentication service.
"""
from sqlalchemy.orm import Session
from app.core.security import create_access_token
from app.core.exceptions import EmailAlreadyExists, InvalidCredentials
from app.session import create_session, remove_session
from app.crud import user_crud
from app.schema.auth import UserRegister, UserLogin, LoginResponse, UserInfo
import logging

logger = logging.getLogger(__name__)


class AuthService:
    """Handles user authentication operations."""
    
    def __init__(self, db: Session):
        self.db = db

    def register_user(self, user_data: UserRegister) -> None:
        """Register a new user."""
        if user_crud.get_by_email(self.db, user_data.email):
            raise EmailAlreadyExists()

        user = user_crud.create(self.db, obj_in=user_data)
        logger.info(f"User registered: {user.email}")

    def login(self, login_data: UserLogin) -> LoginResponse:
        """Authenticate user, create session, return JWT."""
        user = user_crud.authenticate(self.db, login_data.email, login_data.password)
        if not user:
            raise InvalidCredentials()

        access_token = create_access_token(
            data={"sub": str(user.id), "email": user.email}
        )

        user_data = {
            "user_id": str(user.id),
            "email": user.email,
            "is_active": user.is_active,
        }
        create_session(access_token, user_data)

        logger.info(f"User logged in: {user.email}")

        return LoginResponse(
            message="Login successful",
            access_token=access_token,
            user=UserInfo(id=str(user.id), email=user.email, is_active=user.is_active)
        )

    def logout(self, token: str) -> bool:
        """Remove session (invalidate token)."""
        return remove_session(token)
