from sqlalchemy.orm import Session
from uuid import UUID
from app.schemas.restaurant import RestaurantCreate
from app.models.restaurant import Restaurant
from app.crud.restaurant import create_restaurant as crud_create_restaurant


def create_restaurant_service(
    db: Session, data: RestaurantCreate, partner_id: UUID
) -> Restaurant:
    # Any pre-processing or validation can happen here

    restaurant_dict = {
        "partner_id": partner_id,
        "name": data.name,
        "description": data.description,
        "image_url": data.image_url,
        "address_line1": data.address_line1,
        "address_line2": data.address_line2,
        "area": data.area,
        "city": data.city,
        "state": data.state,
        "pincode": data.pincode,
        "latitude": data.latitude,
        "longitude": data.longitude,
        "opening_hours": (
            data.opening_hours.model_dump() if data.opening_hours else None
        ),
        "approval_status": "pending",
        "is_active": True,
    }

    return crud_create_restaurant(db=db, restaurant_data=restaurant_dict)
