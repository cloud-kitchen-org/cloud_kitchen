from uuid import uuid4
from sqlalchemy.orm import Session
from app.enums.user_roles import UserRole
from app.schemas.user import UserCreate, UserOut
from app.crud import user as crud_user
from app.crud.roles import get_role_id_by_name
from app.models.user import User
from typing import Optional, List

from app.utils.hashing import hash_password


# Create a new user
def create_user(db: Session, user_data: UserCreate) -> UserOut:
    existing_email = crud_user.get_user_by_email(db, user_data.email)
    if existing_email:
        raise ValueError("Email already registered")

    existing_phone = crud_user.get_user_by_phone(db, user_data.phone)
    if existing_phone:
        raise ValueError("Phone already registered")

    # Validate role name using enum
    try:
        role_enum = UserRole[user_data.role.upper()]
    except KeyError:
        raise ValueError("Invalid role")

    # Fetch role_id from DB
    role_id = get_role_id_by_name(db, role_enum.value)
    if not role_id:
        raise ValueError("Role not found in database")

    # Create user instance
    user = User(
        id=uuid4(),
        full_name=user_data.full_name,
        email=user_data.email,
        phone=user_data.phone,
        password_hash=hash_password(user_data.password),
        role_id=role_id,
    )
    user = crud_user.create_user(db, user)

    # Ensure role name is returned as string in response
    role_name = user.role.name if hasattr(user.role, "name") else user.role
    return UserOut(
        id=user.id,
        full_name=user.full_name,
        email=user.email,
        phone=user.phone,
        role=role_name,
        is_active=user.is_active,
        created_at=user.created_at,
    )


# Fetch user by ID
def get_user_by_id(db: Session, user_id: str) -> Optional[UserOut]:
    user = crud_user.get_user(db, user_id)
    if user:
        role_name = user.role.name if hasattr(user.role, "name") else user.role
        return UserOut(
            id=user.id,
            full_name=user.full_name,
            email=user.email,
            phone=user.phone,
            role=role_name,
            is_active=user.is_active,
            created_at=user.created_at,
        )
    return None


# List users with pagination
def list_users(db: Session, skip: int = 0, limit: int = 100) -> List[UserOut]:
    users = crud_user.get_users(db, skip=skip, limit=limit)
    return [
        UserOut(
            id=user.id,
            full_name=user.full_name,
            email=user.email,
            phone=user.phone,
            role=user.role.name if hasattr(user.role, "name") else user.role,
            is_active=user.is_active,
            created_at=user.created_at,
        )
        for user in users
    ]


# Deactivate user
def deactivate_user_by_id(db: Session, user_id: str) -> Optional[UserOut]:
    user = crud_user.deactivate_user(db, user_id)
    if user:
        return UserOut(
            id=user.id,
            full_name=user.full_name,
            email=user.email,
            phone=user.phone,
            role=user.role.name if hasattr(user.role, "name") else user.role,
            is_active=user.is_active,
            created_at=user.created_at,
        )
    return None
