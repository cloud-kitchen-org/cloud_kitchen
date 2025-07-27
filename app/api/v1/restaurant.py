from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.current_user import CurrentUser
from app.schemas.restaurant import RestaurantCreate, RestaurantOut, RestaurantSummaryOut
from app.services import restaurant as restaurant_service
from app.api import dependencies as deps

router = APIRouter(prefix="/partner/restaurants", tags=["Partner - Restaurants"])


@router.post("/", response_model=RestaurantOut, status_code=status.HTTP_201_CREATED)
def create_restaurant(
    restaurant_in: RestaurantCreate,
    current_partner: CurrentUser = Depends(deps.get_current_partner_user),
    db: Session = Depends(get_db),
):
    """
    Create a new restaurant profile (basic info only) for a partner.
    """
    restaurant = restaurant_service.create_restaurant_service(
        db=db, data=restaurant_in, partner_id=current_partner.user_id
    )
    return restaurant


@router.get("/", response_model=List[RestaurantSummaryOut])
def get_my_restaurants(
    db: Session = Depends(get_db),
    current_partner: CurrentUser = Depends(deps.get_current_partner_user),
):
    restaurants = restaurant_service.get_restaurants_summary_by_partner_service(
        db, current_partner.user_id
    )
    return restaurants
