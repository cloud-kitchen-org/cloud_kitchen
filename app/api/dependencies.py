import uuid
from fastapi import Depends, HTTPException, status
from app.enums.user_roles import UserRole
from app.schemas.current_user import CurrentUser
from app.utils.token import decode_access_token


def get_current_user(token: str) -> CurrentUser:
    payload = decode_access_token(token)
    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token"
        )
    current_user = CurrentUser(**payload)
    return current_user


def get_current_partner_user(
    current_user: CurrentUser = Depends(get_current_user),
) -> CurrentUser:
    if not current_user.role or current_user.role != UserRole.PARTNER.value:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only partners are allowed.",
        )
    # Convert user_id back to UUID
    current_user.user_id = uuid.UUID(current_user.user_id)
    return current_user
