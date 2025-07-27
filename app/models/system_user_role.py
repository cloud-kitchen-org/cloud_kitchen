import uuid
from datetime import datetime, timezone
from sqlalchemy import Boolean, Column, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.db.base import Base
from app.utils.time import utcnow_column


class SystemUserRole(Base):
    __tablename__ = "system_user_roles"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    system_user_id = Column(
        UUID(as_uuid=True), ForeignKey("system_users.id", ondelete="CASCADE"), nullable=False
    )
    role_id = Column(UUID(as_uuid=True), ForeignKey("roles.id", ondelete="CASCADE"), nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    created_at = utcnow_column()

    system_user = relationship("SystemUser", back_populates="roles")
    role = relationship("Role", back_populates="system_user_roles")
