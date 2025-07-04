from pydantic import BaseModel, EmailStr
from uuid import UUID


class CurrentUser(BaseModel):
    user_id: UUID
    email: EmailStr
    role: str
