from pydantic import BaseModel, EmailStr, Field
from uuid import UUID
from typing import Optional
from datetime import datetime


class UserBase(BaseModel):
    full_name: str
    email: EmailStr | None = None
    phone: str = Field(..., min_length=10, max_length=10)
    role: str = Field(..., description="Role ID or name")


class UserCreate(UserBase):
    password: str = Field(..., min_length=4)


class UserOut(BaseModel):
    id: UUID
    full_name: str
    email: EmailStr | None = None
    phone: str
    role: str
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True


class UserUpdate(BaseModel):
    full_name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = Field(default=None, min_length=10, max_length=10)
    role: Optional[str] = None
    is_active: Optional[bool] = None
