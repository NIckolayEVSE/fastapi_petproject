from datetime import date

from pydantic import BaseModel


class SBooking(BaseModel):
    room_id: int
    date_from: date
    date_to: date


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
