from sqlalchemy.orm import Session
from app.models.restaurant import Restaurant
from app.schemas.restaurant import RestaurantCreate
import uuid


def get_restaurant_by_name(db: Session, name: str):
    return db.query(Restaurant).filter(Restaurant.name == name).first()


def create_restaurant_db(db: Session, data: RestaurantCreate, partner_id: str):
    restaurant = Restaurant(id=str(uuid.uuid4()), partner_id=partner_id, **data.dict())
    db.add(restaurant)
    db.commit()
    db.refresh(restaurant)
    return restaurant
