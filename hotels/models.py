from sqlalchemy import Column, Integer, String, JSON, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base


class Hotels(Base):
    __tablename__ = "hotels"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    location: Mapped[str] = mapped_column(nullable=False)
    services: Mapped[dict[list]] = mapped_column(type_=JSON)
    room_quantity: Mapped[int] = mapped_column(nullable=False)
    image_id: Mapped[int]
    rooms_rel: Mapped[int] = relationship(
        back_populates="hotel", cascade="all, delete-orphan"
    )


class Rooms(Base):
    __tablename__ = "rooms"

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    hotel_id: Mapped[int] = mapped_column(ForeignKey("hotels.id"), nullable=False)
    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)
    price: Mapped[int] = mapped_column(nullable=False)
    services: Mapped[dict[list]] = mapped_column(type_=JSON, nullable=True)
    quantity: Mapped[int] = mapped_column(nullable=False)
    image_id: Mapped[int]
    hotel: Mapped[int] = relationship(back_populates="rooms_rel")
