from pydantic import BaseModel
from typing import Optional
from uuid import UUID


class DayHours(BaseModel):
    open_time: Optional[str] = None  # e.g. "09:00"
    close_time: Optional[str] = None  # e.g. "22:00"
    is_closed: bool = False


class RestaurantOpeningHours(BaseModel):
    monday: Optional[DayHours]
    tuesday: Optional[DayHours]
    wednesday: Optional[DayHours]
    thursday: Optional[DayHours]
    friday: Optional[DayHours]
    saturday: Optional[DayHours]
    sunday: Optional[DayHours]


class RestaurantBase(BaseModel):
    name: str
    description: Optional[str] = None
    image_url: Optional[str] = None
    address_line1: str
    address_line2: Optional[str] = None
    area: str
    city: str
    state: str
    pincode: str
    latitude: float
    longitude: float
    opening_hours: Optional[RestaurantOpeningHours] = None


class RestaurantCreate(RestaurantBase):
    pass


class RestaurantOut(RestaurantBase):
    id: UUID
    approval_status: str

    class Config:
        from_attributes = True


class RestaurantSummaryOut(BaseModel):
    id: UUID
    name: str
    image_url: Optional[str] = None
    area: str
    city: str
    state: str
    approval_status: str

    class Config:
        from_attributes = True
