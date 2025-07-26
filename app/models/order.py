from sqlalchemy import Column, String, ForeignKey, DateTime, DECIMAL
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from app.db.base import Base
from app.utils.time import utcnow_column
import uuid
from datetime import datetime, timezone


class Order(Base):
    __tablename__ = "orders"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    restaurant_id = Column(UUID(as_uuid=True), ForeignKey("restaurants.id"), nullable=False)
    address_id = Column(UUID(as_uuid=True), ForeignKey("user_addresses.id"), nullable=False)
    status = Column(String(20), default="PLACED", nullable=False)
    total_amount = Column(DECIMAL(10, 2), nullable=False)
    payment_status = Column(String(20), default="PENDING", nullable=False)
    delivery_type = Column(String(20), default="delivery", nullable=False)
    created_at = utcnow_column()
    updated_at = utcnow_column(onupdate=True)

    user = relationship("User", back_populates="orders")
    restaurant = relationship("Restaurant", back_populates="orders")
    address = relationship("UserAddress", back_populates="orders")
    order_items = relationship(
        "OrderItem", back_populates="order", cascade="all, delete-orphan"
    )
    payment = relationship("Payment", back_populates="order", uselist=False)
