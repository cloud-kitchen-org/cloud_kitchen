from sqlalchemy.orm import Session
from app.schemas.user import UserCreate
from app.crud import user as crud_user
from app.models.user import User
from typing import Optional, List


# Create a new user
def register_user(db: Session, user_data: UserCreate) -> User:
    existing_email = crud_user.get_user_by_email(db, user_data.email)
    if existing_email:
        raise ValueError("Email already registered")

    existing_phone = crud_user.get_user_by_phone(db, user_data.phone)
    if existing_phone:
        raise ValueError("Phone already registered")

    return crud_user.create_user(db, user_data)


# Fetch user by ID
def get_user_by_id(db: Session, user_id: str) -> Optional[User]:
    return crud_user.get_user(db, user_id)


# List users with pagination
def list_users(db: Session, skip: int = 0, limit: int = 100) -> List[User]:
    return crud_user.get_users(db, skip=skip, limit=limit)


# Deactivate user
def deactivate_user_by_id(db: Session, user_id: str) -> Optional[User]:
    return crud_user.deactivate_user(db, user_id)
