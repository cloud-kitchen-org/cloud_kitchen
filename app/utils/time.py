from sqlalchemy import Column, DateTime
from datetime import datetime, timezone


def utcnow_column(onupdate=False):
    """
    Returns a SQLAlchemy DateTime column with UTC timezone.
    If onupdate=True, sets onupdate to current UTC time for updated_at fields.
    Usage:
        created_at = utcnow_column()
        updated_at = utcnow_column(onupdate=True)
    """
    if onupdate:
        return Column(
            DateTime(timezone=True),
            default=datetime.now(tz=timezone.utc),
            onupdate=datetime.now(tz=timezone.utc),
        )
    return Column(DateTime(timezone=True), default=datetime.now(tz=timezone.utc))
