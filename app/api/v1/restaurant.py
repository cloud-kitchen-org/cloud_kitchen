from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.current_user import CurrentUser
from app.schemas.restaurant import RestaurantCreate, RestaurantOut
from app.db.session import get_db
from app.api.deps import get_current_user
from app.services.restaurant import register_restaurant

router = APIRouter(prefix="/restaurants", tags=["Restaurants"])


@router.post("/", response_model=RestaurantOut)
def create_restaurant(
    data: RestaurantCreate,
    db: Session = Depends(get_db),
    current_user: CurrentUser = Depends(get_current_user),
):
    pass
