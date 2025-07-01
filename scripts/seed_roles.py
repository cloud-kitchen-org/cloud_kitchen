from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.role import Role
from datetime import datetime, timezone
import uuid


def seed_roles():
    db: Session = SessionLocal()

    default_roles = [
        {"name": "admin", "description": "Administrator Role"},
        {"name": "partner", "description": "Restaurant Partner"},
        {"name": "user", "description": "Application User"},
    ]

    for role in default_roles:
        existing = db.query(Role).filter_by(name=role["name"]).first()
        if not existing:
            db.add(
                Role(
                    id=uuid.uuid4(),
                    name=role["name"],
                    description=role["description"],
                    created_at=datetime.now(tz=timezone.utc),
                )
            )

    db.commit()
    db.close()
    print("Seeded default roles.")


if __name__ == "__main__":
    seed_roles()
