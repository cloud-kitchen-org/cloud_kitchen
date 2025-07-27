from sqlalchemy import Column, ForeignKey, String, Boolean, Text, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.db.base import Base
from app.utils.time import utcnow_column
import uuid


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    full_name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    phone = Column(String(15), unique=True, nullable=False)
    password_hash = Column(Text, nullable=False)
    role_id = Column(UUID(as_uuid=True), ForeignKey("roles.id"), nullable=True)
    is_active = Column(Boolean, default=True, nullable=False)
    created_at = utcnow_column()
    updated_at = utcnow_column(onupdate=True)

    role = relationship("Role", back_populates="users")
    addresses = relationship(
        "UserAddress", back_populates="user", cascade="all, delete-orphan"
    )
    orders = relationship("Order", back_populates="user")
    restaurants = relationship("Restaurant", back_populates="partner")
    cart_items = relationship("CartItem", back_populates="user")
