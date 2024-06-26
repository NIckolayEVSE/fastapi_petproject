from datetime import datetime, timedelta

from jose import jwt
from passlib.context import CryptContext
from pydantic import EmailStr

from config import settings
from users.dao import UserService
from users.schemas import SUserAuthDB


pwd_contex = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto",
)


def get_password_hash(password: str):
    return pwd_contex.hash(password)


def verify_password(plain_password, hashed_password) -> bool:
    return pwd_contex.verify(plain_password, hashed_password)


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode,
        settings.SECRET_KEY,
        settings.ALGORITHM,
    )
    return encoded_jwt


async def authenticate_user(email: EmailStr, password: str):
    user = await UserService.find_one_or_none(email=email)
    if user:
        user = SUserAuthDB(
            id=user["Users"].id,
            email=user["Users"].email,
            hashed_password=user["Users"].hashed_password,
        )
        if verify_password(password, user.hashed_password):
            return user
