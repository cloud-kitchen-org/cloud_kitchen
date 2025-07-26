# 📁 app/api/v1/user.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID

from app.schemas.user import UserCreate, UserOut
from app.services import user as user_service
from app.db.session import get_db

router = APIRouter(prefix="/users", tags=["Users"])


# Register new user
@router.post("/", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def create_user(user_in: UserCreate, db: Session = Depends(get_db)):
    try:
        return user_service.create_user(db, user_in)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


# Get user by ID
@router.get("/{user_id}", response_model=UserOut)
def get_user(user_id: UUID, db: Session = Depends(get_db)):
    user = user_service.get_user_by_id(db, str(user_id))
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


# List users (optional pagination)
@router.get("/", response_model=List[UserOut])
def list_all_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return user_service.list_users(db, skip=skip, limit=limit)


# Deactivate user
@router.delete("/{user_id}", response_model=UserOut)
def deactivate_user(user_id: UUID, db: Session = Depends(get_db)):
    user = user_service.deactivate_user_by_id(db, str(user_id))
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
