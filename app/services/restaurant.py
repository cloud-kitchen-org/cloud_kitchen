from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.schemas.restaurant import RestaurantCreate
from app.crud.restaurant import create_restaurant_db, get_restaurant_by_name


def register_restaurant(data: RestaurantCreate, partner_id: str, db: Session):
    existing = get_restaurant_by_name(db, data.name)
    if existing:
        raise HTTPException(status_code=400, detail="Restaurant already exists")

    return create_restaurant_db(db, data, partner_id)
