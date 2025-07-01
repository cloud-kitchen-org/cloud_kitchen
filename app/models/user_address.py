from sqlalchemy import Column, String, Text, Boolean, ForeignKey, DateTime, DECIMAL
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from app.db.base import Base
from app.utils.time import utcnow_column
import uuid
from datetime import datetime, timezone


class UserAddress(Base):
    __tablename__ = "user_addresses"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    label = Column(String(50))
    address_line1 = Column(Text)
    address_line2 = Column(Text)
    area = Column(String(100))
    city = Column(String(100))
    state = Column(String(100))
    pincode = Column(String(10))
    latitude = Column(DECIMAL(9, 6))
    longitude = Column(DECIMAL(9, 6))
    is_default = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    created_at = utcnow_column()

    user = relationship("User", back_populates="addresses")
    orders = relationship("Order", back_populates="address")
