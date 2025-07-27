from typing import List
from uuid import UUID
from sqlalchemy.orm import Session
from app.models.restaurant import Restaurant


def create_restaurant(db: Session, restaurant: Restaurant) -> Restaurant:
    db.add(restaurant)
    db.commit()
    db.refresh(restaurant)
    return restaurant


def get_restaurants_by_partner(db: Session, partner_id: UUID) -> List[Restaurant]:
    return (
        db.query(Restaurant)
        .filter(Restaurant.partner_id == partner_id, Restaurant.is_active == True)
        .all()
    )
