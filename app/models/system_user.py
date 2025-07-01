import uuid
from datetime import datetime, timezone
from sqlalchemy import Column, String, Boolean, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.db.base import Base
from app.utils.time import utcnow_column


class SystemUser(Base):
    __tablename__ = "system_users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    full_name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = utcnow_column()
    updated_at = utcnow_column()

    roles = relationship(
        "SystemUserRole", back_populates="system_user", cascade="all, delete-orphan"
    )
