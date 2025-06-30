from sqlalchemy import Column, Integer, ForeignKey, DateTime, DECIMAL
from sqlalchemy.orm import relationship
from app.db.base import Base
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime, timezone


class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    order_id = Column(UUID(as_uuid=True), ForeignKey("orders.id", ondelete="CASCADE"))
    item_id = Column(UUID(as_uuid=True), ForeignKey("items.id"))
    quantity = Column(Integer, nullable=False)
    price_at_order_time = Column(DECIMAL(10, 2))
    created_at = Column(DateTime, default=datetime.now(tz=timezone.utc))

    order = relationship("Order", back_populates="order_items")
    item = relationship("Item", back_populates="order_items")
