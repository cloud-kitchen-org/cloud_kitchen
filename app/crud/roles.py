from sqlalchemy.orm import Session
from app.models.role import Role

def get_role_id_by_name(db: Session, role_name: str):
    role = db.query(Role).filter(Role.name == role_name).first()
    if role:
        return role.id
    return None
