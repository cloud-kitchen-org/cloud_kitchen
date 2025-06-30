from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.db.base import Base
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime, timezone


class CartItem(Base):
    __tablename__ = "cart_items"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"))
    restaurant_id = Column(UUID(as_uuid=True), ForeignKey("restaurants.id"))
    item_id = Column(UUID(as_uuid=True), ForeignKey("items.id"))
    quantity = Column(Integer, default=1)
    created_at = Column(DateTime, default=datetime.now(tz=timezone.utc))

    user = relationship("User", back_populates="cart_items")
    restaurant = relationship("Restaurant", back_populates="cart_items")
    item = relationship("Item", back_populates="cart_items")
