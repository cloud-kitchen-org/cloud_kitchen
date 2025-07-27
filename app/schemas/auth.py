from pydantic import BaseModel


class LoginRequestByEmail(BaseModel):
    email: str
    password: str


class LoginRequestByPhone(BaseModel):
    phone: str
    otp: str


class LoginResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
