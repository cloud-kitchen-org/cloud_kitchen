from sqlalchemy.orm import Session
from app.models.user import User
from typing import Optional


# Create user
def create_user(db: Session, user: User) -> User:
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


# Get user by email
def get_user_by_email(db: Session, email: str) -> Optional[User]:
    return db.query(User).filter(User.email == email).first()


# Get user by phone
def get_user_by_phone(db: Session, phone: str) -> Optional[User]:
    return db.query(User).filter(User.phone == phone).first()


# Get user by id
def get_user(db: Session, user_id: str) -> Optional[User]:
    return db.query(User).filter(User.id == user_id).first()


# List all users (optional pagination)
def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


# Deactivate or soft delete user
def deactivate_user(db: Session, user_id: str) -> Optional[User]:
    user = get_user(db, user_id)
    if user:
        user.is_active = False
        db.commit()
        db.refresh(user)
    return user
