from fastapi import APIRouter, Depends
from sqlalchemy import select

from booking.dao import BookingDAO
from booking.models import Bookings
from database import async_session_maker
from schemas import SBooking
from users.dependencies import get_current_user
from users.models import Users

router = APIRouter(
    prefix="/bookings",
    tags=["Бронирование"],
)


@router.get("")
async def get_booking(user: Users = Depends(get_current_user)) -> list[SBooking]:
    return await BookingDAO.find_all(user_id=user.id)


@router.post("/")
async def add_booking(user: Users = Depends(get_current_user)):
    await BookingDAO.add()
