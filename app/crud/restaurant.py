from sqlalchemy.orm import Session
from app.models.restaurant import Restaurant


def create_restaurant(db: Session, restaurant_data: dict) -> Restaurant:
    new_restaurant = Restaurant(**restaurant_data)
    db.add(new_restaurant)
    db.commit()
    db.refresh(new_restaurant)
    return new_restaurant
