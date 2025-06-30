from sqlalchemy import (
    Column,
    String,
    Text,
    Boolean,
    ForeignKey,
    DateTime,
    DECIMAL,
    ARRAY,
)
from sqlalchemy.orm import relationship
from app.db.base import Base
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime, timezone


class Item(Base):
    __tablename__ = "items"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    category_id = Column(
        UUID(as_uuid=True), ForeignKey("categories.id", ondelete="CASCADE")
    )
    name = Column(String(100), nullable=False)
    description = Column(Text)
    price = Column(DECIMAL(10, 2), nullable=False)
    image_url = Column(Text)
    tax_percentage = Column(DECIMAL(5, 2), default=0.00)
    tags = Column(ARRAY(Text))
    is_available = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.now(tz=timezone.utc))
    updated_at = Column(DateTime, default=datetime.now(tz=timezone.utc))

    category = relationship("Category", back_populates="items")
    cart_items = relationship("CartItem", back_populates="item")
    order_items = relationship("OrderItem", back_populates="item")
