from sqlalchemy.orm import Session
from typing import Optional
from app.models.user import User
from app.crud import user as crud_user
from app.utils.hashing import verify_password


def authenticate_user(db: Session, email: str, password: str) -> Optional[User]:
    user = crud_user.get_user_by_email(db, email)
    if user and verify_password(password, user.password_hash):
        return user
    return None
