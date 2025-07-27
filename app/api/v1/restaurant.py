from typing import List
from fastapi import APIRouter, Depends, status
from uuid import UUID
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.current_user import CurrentUser
from app.schemas.restaurant import (
    RestaurantCreate,
    RestaurantOut,
    RestaurantSummaryOut,
    RestaurantUpdate,
)
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
    """
    Retrieve all active restaurants for the current partner.
    """
    restaurants = restaurant_service.get_restaurants_summary_by_partner_service(
        db, current_partner.user_id
    )
    return restaurants


@router.get("/{restaurant_id}", response_model=RestaurantOut)
def get_restaurant_details(
    restaurant_id: UUID,
    db: Session = Depends(get_db),
    current_user: CurrentUser = Depends(deps.get_current_partner_user),
):
    """
    Retrieve detailed information about a specific restaurant by its ID.
    """
    return restaurant_service.get_restaurant_details_by_id_service(
        db, current_user.user_id, restaurant_id
    )


@router.put("/{restaurant_id}", response_model=RestaurantOut)
def update_restaurant(
    restaurant_id: UUID,
    restaurant_data: RestaurantUpdate,
    db: Session = Depends(get_db),
    current_user: CurrentUser = Depends(deps.get_current_partner_user),
):
    """
    Update an existing restaurant's information.
    """
    return restaurant_service.update_restaurant_data_service(
        db, current_user.user_id, restaurant_id, restaurant_data
    )


@router.delete("/{restaurant_id}", status_code=204)
def delete_restaurant(
    restaurant_id: UUID,
    db: Session = Depends(get_db),
    current_user: CurrentUser = Depends(deps.get_current_partner_user),
):
    """
    Delete a restaurant.
    """
    restaurant_service.delete_restaurant_service(
        db, current_user.user_id, restaurant_id
    )
