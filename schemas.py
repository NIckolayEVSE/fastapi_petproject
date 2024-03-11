from datetime import date

from pydantic import BaseModel


class SBooking(BaseModel):
    id: int
    room_id: int
    user_id: int
    date_from: date
    date_to: date
    price: int
    total_cost: int
    total_days: int

    class Config:
        from_attributes = True


class SHotel(BaseModel):
    address: str
    name: str
    stars: int


class GetHotels(BaseModel):
    location: str
    date_from: date
    date_to: date
    has_spa: bool = None
    stars: int = None
