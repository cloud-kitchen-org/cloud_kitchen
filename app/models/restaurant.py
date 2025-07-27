from sqlalchemy import (
    Column,
    String,
    Text,
    Boolean,
    ForeignKey,
    JSON,
    ARRAY,
    DECIMAL,
)
from sqlalchemy.orm import relationship
from app.db.base import Base
from sqlalchemy.dialects.postgresql import UUID
import uuid

from app.utils.time import utcnow_column


class Restaurant(Base):
    __tablename__ = "restaurants"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    partner_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    name = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    image_url = Column(Text, nullable=True)
    cuisine_tags = Column(ARRAY(Text), nullable=True)
    address_line1 = Column(Text, nullable=True)
    address_line2 = Column(Text, nullable=True)
    area = Column(String(100), nullable=True)
    city = Column(String(100), nullable=True)
    state = Column(String(100), nullable=True)
    pincode = Column(String(10), nullable=True)
    latitude = Column(DECIMAL(9, 6), nullable=True)
    longitude = Column(DECIMAL(9, 6), nullable=True)
    opening_hours = Column(JSON, nullable=True)
    approval_status = Column(String(20), default="pending", nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    created_at = utcnow_column()
    updated_at = utcnow_column(onupdate=True)

    partner = relationship("User", back_populates="restaurants")
    orders = relationship("Order", back_populates="restaurant")
    cart_items = relationship("CartItem", back_populates="restaurant")
    menu_sections = relationship(
        "MenuSection", back_populates="restaurant", cascade="all, delete-orphan"
    )
