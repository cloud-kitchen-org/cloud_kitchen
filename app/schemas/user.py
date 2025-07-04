from pydantic import BaseModel, EmailStr, Field
from uuid import UUID
from typing import Optional
from datetime import datetime


class UserBase(BaseModel):
    full_name: str
    email: EmailStr
    phone: str = Field(..., min_length=10, max_length=15)
    role: str


class UserCreate(UserBase):
    password: str = Field(..., min_length=6)


class UserOut(BaseModel):
    id: UUID
    full_name: str
    email: EmailStr
    phone: str
    role: str
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True


class UserUpdate(BaseModel):
    full_name: Optional[str] = None
    phone: Optional[str] = Field(default=None, min_length=10, max_length=15)
    is_active: Optional[bool] = None
