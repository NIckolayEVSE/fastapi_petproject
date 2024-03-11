from datetime import date

import uvicorn
from fastapi import FastAPI, Query

from booking.router import router as router_booking
from schemas import SHotel
from users.router import router as router_users

app = FastAPI(
    title="Trading App",
)

app.include_router(router_users)
app.include_router(router_booking)


@app.get("/hotel/", response_model=list[SHotel])
async def get_hostels(
    # obj: GetHotels,
    location: str,
    date_from: date,
    date_to: date,
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


# @app.post("/bookings")
# async def add_booking(booking: SBooking):
#     pass


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
