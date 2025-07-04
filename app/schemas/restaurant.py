from pydantic import BaseModel
from typing import List, Optional


class RestaurantCreate(BaseModel):
    name: str
    description: Optional[str]
    image_url: Optional[str]
    cuisine_tags: List[str]
    address_line1: str
    address_line2: Optional[str]
    area: str
    city: str
    state: str
    pincode: str
    latitude: float
    longitude: float
    opening_hours: dict


class RestaurantOut(RestaurantCreate):
    id: str
    approval_status: str
