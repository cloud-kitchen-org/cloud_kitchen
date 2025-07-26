from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.user import User
from app.schemas.auth import LoginRequestByEmail, LoginRequestByPhone, LoginResponse
from app.schemas.current_user import CurrentUser
from app.utils.token import create_access_token
from app.services import auth as auth_service

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/login-email", response_model=LoginResponse)
def login(login_request: LoginRequestByEmail, db: Session = Depends(get_db)):
    user: User = auth_service.authenticate_user(
        db, login_request.email, login_request.password
    )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials"
        )

    user_data = CurrentUser(
        user_id=str(user.id), email=user.email, phone=user.phone, role=user.role.name
    )
    token = create_access_token(data=user_data.model_dump())
    return {"access_token": token, "token_type": "bearer"}


@router.post("/login-phone", response_model=LoginResponse)
def login_phone(login_request: LoginRequestByPhone, db: Session = Depends(get_db)):
    user: User = auth_service.authenticate_user_by_phone(
        db, login_request.phone, login_request.otp
    )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials"
        )

    user_data = CurrentUser(
        user_id=str(user.id), email=user.email, phone=user.phone, role=user.role.name
    )
    token = create_access_token(data=user_data.model_dump())
    return {"access_token": token, "token_type": "bearer"}
