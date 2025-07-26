from pydantic import BaseModel, EmailStr
from uuid import UUID


class CurrentUser(BaseModel):
    user_id: str | UUID
    email: EmailStr | None = None
    phone: str
    role: str
