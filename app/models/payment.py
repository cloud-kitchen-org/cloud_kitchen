from sqlalchemy import Column, String, ForeignKey, DateTime, DECIMAL, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from app.db.base import Base
from app.utils.time import utcnow_column
import uuid
from datetime import datetime, timezone


class Payment(Base):
    __tablename__ = "payments"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    order_id = Column(UUID(as_uuid=True), ForeignKey("orders.id"))
    provider = Column(String(50))
    transaction_id = Column(String(100))
    amount = Column(DECIMAL(10, 2))
    currency = Column(String(10), default="INR")
    status = Column(String(20))
    paid_at = Column(DateTime)
    payment_metadata = Column(JSON)
    created_at = utcnow_column()

    order = relationship("Order", back_populates="payment")
