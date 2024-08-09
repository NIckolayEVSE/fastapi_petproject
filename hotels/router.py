import datetime

from fastapi import APIRouter, Query

from schemas import SHotel

router = APIRouter(
    prefix="/hotel",
    tags=["Отели"],
)


@router.get("/hotel/", response_model=list[SHotel])
async def get_hostels(
    # obj: GetHotels,
    location: str,
    date_from: datetime.date,
    date_to: datetime.date,
    has_spa: bool = None,
    stars=Query(None, ge=1, le=5),
):
    hotels = [
        {
            "address": "ул. Гагарина, 1, Щелково",
            "name": "Hotel",
            "stars": 5,
        }
    ]
    return hotels
