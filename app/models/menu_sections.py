from sqlalchemy import (
    Column,
    String,
    ForeignKey,
    Integer,
)
from sqlalchemy.orm import relationship
from app.db.base import Base
from sqlalchemy.dialects.postgresql import UUID
import uuid

from app.utils.time import utcnow_column


class MenuSection(Base):
    __tablename__ = "menu_sections"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    restaurant_id = Column(
        UUID(as_uuid=True), ForeignKey("restaurants.id", ondelete="CASCADE"), nullable=False
    )
    name = Column(String(100), nullable=False)  # E.g., "Breakfast", "Navratri Specials"
    description = Column(String, nullable=True)
    sort_order = Column(Integer, default=0, nullable=False)
    created_at = utcnow_column()
    updated_at = utcnow_column(onupdate=True)

    restaurant = relationship("Restaurant", back_populates="menu_sections")
    items = relationship("Item", back_populates="section", cascade="all, delete-orphan")
