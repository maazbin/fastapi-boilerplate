"""
User CRUD operations.
"""
from typing import Optional
from sqlalchemy.orm import Session
from app.model.user import User
from app.schema.user import UserCreate
from app.core.security import get_password_hash, check_password
from app.crud.base import CRUDBase


class CRUDUser(CRUDBase[User, UserCreate, dict]):
    """User-specific CRUD operations."""
    
    def get_by_email(self, db: Session, email: str) -> Optional[User]:
        """Get user by email."""
        return self.get_by_field(db, "email", email)

    def create(self, db: Session, *, obj_in: UserCreate) -> User:
        """Create user with hashed password."""
        user_data = {
            "email": obj_in.email,
            "password_hash": get_password_hash(obj_in.password)
        }
        return self.create_from_dict(db, obj_in=user_data)

    def authenticate(self, db: Session, email: str, password: str) -> Optional[User]:
        """Authenticate user by email and password."""
        user = self.get_by_email(db, email)
        if not user:
            return None
        if not check_password(password, user.password_hash):
            return None
        return user


user_crud = CRUDUser(User)
