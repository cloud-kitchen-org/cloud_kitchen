from sqlalchemy import Column, DateTime
from datetime import datetime, timezone


def utcnow_column():
    return Column(DateTime(timezone=True), default=datetime.now(tz=timezone.utc))
