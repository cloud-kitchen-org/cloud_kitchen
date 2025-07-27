from typing import List, Optional
from uuid import UUID
from sqlalchemy.orm import Session
from app.models.restaurant import Restaurant


def create_restaurant(db: Session, restaurant: Restaurant) -> Restaurant:
    db.add(restaurant)
    db.commit()
    db.refresh(restaurant)
    return restaurant


def get_restaurants_by_partner(db: Session, partner_id: UUID) -> List[Restaurant]:
    return db.query(Restaurant).filter(Restaurant.partner_id == partner_id).all()


def get_restaurant_by_id(
    db: Session, partner_id: UUID, restaurant_id: UUID
) -> Optional[Restaurant]:
    return (
        db.query(Restaurant)
        .filter(Restaurant.id == restaurant_id, Restaurant.partner_id == partner_id)
        .first()
    )


def update_restaurant(db: Session, restaurant: Restaurant) -> Restaurant:
    db.commit()
    db.refresh(restaurant)
    return restaurant


def delete_restaurant(db: Session, restaurant: Restaurant):
    db.delete(restaurant)
    db.commit()
