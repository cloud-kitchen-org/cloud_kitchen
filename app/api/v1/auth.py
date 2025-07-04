from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.current_user import CurrentUser
from app.utils.token import create_access_token
from app.services import auth as auth_service

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    user = auth_service.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials"
        )

    user_data = CurrentUser(user_id=user.id, email=user.email, role=user.role.name)
    token = create_access_token(data=user_data.model_dump())
    return {"access_token": token, "token_type": "bearer"}
