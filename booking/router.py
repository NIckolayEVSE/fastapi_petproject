from fastapi import APIRouter
from sqlalchemy import select

from booking.dao import BookingDAO
from booking.models import Bookings
from database import async_session_maker

router = APIRouter(
    prefix="/bookings",
    tags=["Бронирование"],
)


@router.get("")
async def get_booking():
    # async with async_session_maker() as session:
    #     query = select(Bookings)
    #     result = await session.execute(query)
    #     return result.mappings().all()
    return await BookingDAO.find_one_or_none(room_id=1)
