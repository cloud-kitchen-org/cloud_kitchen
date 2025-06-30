from sqlalchemy import (
    Column,
    String,
    Text,
    Boolean,
    ForeignKey,
    DateTime,
    JSON,
    ARRAY,
    DECIMAL,
)
from sqlalchemy.orm import relationship
from app.db.base import Base
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime, timezone


class Restaurant(Base):
    __tablename__ = "restaurants"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    partner_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    name = Column(String(100), nullable=False)
    description = Column(Text)
    image_url = Column(Text)
    cuisine_tags = Column(ARRAY(Text))
    address_line1 = Column(Text)
    address_line2 = Column(Text)
    area = Column(String(100))
    city = Column(String(100))
    state = Column(String(100))
    pincode = Column(String(10))
    latitude = Column(DECIMAL(9, 6))
    longitude = Column(DECIMAL(9, 6))
    opening_hours = Column(JSON)
    approval_status = Column(String(20), default="pending")
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.now(tz=timezone.utc))
    updated_at = Column(DateTime, default=datetime.now(tz=timezone.utc))

    partner = relationship("User", back_populates="restaurants")
    categories = relationship(
        "Category", back_populates="restaurant", cascade="all, delete-orphan"
    )
    orders = relationship("Order", back_populates="restaurant")
    cart_items = relationship("CartItem", back_populates="restaurant")
