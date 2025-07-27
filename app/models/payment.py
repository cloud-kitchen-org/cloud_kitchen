from sqlalchemy import Column, String, ForeignKey, DateTime, DECIMAL, JSON, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from app.db.base import Base
from app.utils.time import utcnow_column

import uuid
from datetime import datetime, timezone
import enum


class PaymentStatus(enum.Enum):
    pending = "pending"
    completed = "completed"
    failed = "failed"
    refunded = "refunded"


class Currency(enum.Enum):
    INR = "INR"
    USD = "USD"
    EUR = "EUR"
    GBP = "GBP"


class Payment(Base):
    __tablename__ = "payments"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    order_id = Column(UUID(as_uuid=True), ForeignKey("orders.id"), nullable=False)
    provider = Column(String(50), nullable=True)
    transaction_id = Column(String(100), nullable=True)
    amount = Column(DECIMAL(10, 2), nullable=True)
    currency = Column(Enum(Currency), default=Currency.INR, nullable=False)
    status = Column(Enum(PaymentStatus), default=PaymentStatus.pending, nullable=False)
    paid_at = Column(DateTime, nullable=True)
    payment_metadata = Column(JSON, nullable=True)
    created_at = utcnow_column()

    order = relationship("Order", back_populates="payment")
