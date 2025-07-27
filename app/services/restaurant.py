from sqlalchemy.orm import Session
from uuid import UUID
from app.schemas.restaurant import RestaurantCreate, RestaurantOut, RestaurantSummaryOut
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
