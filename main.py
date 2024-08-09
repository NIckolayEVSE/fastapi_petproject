import uvicorn
from fastapi import FastAPI

from booking.router import router as router_booking
from hotels.router import router as router_hotels
from users.router import router as router_users

app = FastAPI(
    title="Trading App",
)

app.include_router(router_users)
app.include_router(router_booking)
app.include_router(router_hotels)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
