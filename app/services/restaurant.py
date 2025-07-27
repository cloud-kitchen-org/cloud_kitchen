from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from uuid import UUID
from app.schemas.restaurant import (
    RestaurantCreate,
    RestaurantOut,
    RestaurantSummaryOut,
    RestaurantUpdate,
)
from app.models.restaurant import Restaurant
from app.crud import restaurant as crud_restaurant


def create_restaurant_service(
    db: Session, data: RestaurantCreate, partner_id: UUID
) -> RestaurantOut:
    # Any pre-processing or validation can happen here

    restaurant = Restaurant(
        partner_id=partner_id,
        name=data.name,
        description=data.description,
        image_url=data.image_url,
        address_line1=data.address_line1,
        address_line2=data.address_line2,
        area=data.area,
        city=data.city,
        state=data.state,
        pincode=data.pincode,
        latitude=data.latitude,
        longitude=data.longitude,
        opening_hours=data.opening_hours.model_dump() if data.opening_hours else None,
    )

    restaurant = crud_restaurant.create_restaurant(db=db, restaurant=restaurant)
    return RestaurantOut.model_validate(restaurant)


def get_restaurants_summary_by_partner_service(
    db: Session, partner_id: UUID
) -> list[RestaurantSummaryOut]:
    """
    Retrieve all active restaurants for a given partner.
    """
    restaurants = crud_restaurant.get_restaurants_by_partner(
        db=db, partner_id=partner_id
    )
    return [
        RestaurantSummaryOut.model_validate(restaurant) for restaurant in restaurants
    ]


def get_restaurant_details_by_id_service(
    db: Session, partner_id: UUID, restaurant_id: UUID
) -> RestaurantOut:
    restaurant = crud_restaurant.get_restaurant_by_id(db, partner_id, restaurant_id)
    if not restaurant:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Restaurant not found"
        )
    return RestaurantOut.model_validate(restaurant)


def update_restaurant_data_service(
    db: Session,
    partner_id: UUID,
    restaurant_id: UUID,
    updated_restaurant: RestaurantUpdate,
) -> RestaurantOut:
    restaurant = crud_restaurant.get_restaurant_by_id(db, partner_id, restaurant_id)
    if not restaurant:
        raise HTTPException(status_code=404, detail="Restaurant not found")

    for field, value in updated_restaurant.model_dump(exclude_unset=True).items():
        setattr(restaurant, field, value)

    restaurant = crud_restaurant.update_restaurant(db, restaurant)
    return RestaurantOut.model_validate(restaurant)


def delete_restaurant_service(db: Session, partner_id: UUID, restaurant_id: UUID):
    restaurant = crud_restaurant.get_restaurant_by_id(db, partner_id, restaurant_id)
    if not restaurant:
        raise HTTPException(status_code=404, detail="Restaurant not found")

    # If you want to hard delete, uncomment the line below and comment the soft delete logic
    # crud_restaurant.delete_restaurant(db, restaurant)

    # For soft delete, we can set is_active to False
    restaurant.is_active = False
    crud_restaurant.update_restaurant(db, restaurant)
