from booking.models import Bookings
from services.base import BaseService


class BookingDAO(BaseService):
    model = Bookings


