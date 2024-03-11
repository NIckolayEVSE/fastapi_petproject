from fastapi import Request, Depends
from jose import jwt, JWTError

from config import settings

from datetime import datetime

from exceptions import (
    TokenExpiredException,
    TokenAbsentException,
    IncorrectTokenFormat,
    UserNotExistsException,
)
from users.dao import UserService
from users.models import Users


def get_token(request: Request):
    token = request.cookies.get("booking_access_token")
    if not token:
        raise TokenAbsentException()
    return token


async def get_current_user(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            settings.ALGORITHM,
        )
    except JWTError:
        raise IncorrectTokenFormat()
    expire: str = payload.get("exp")
    if not expire or int(expire) < datetime.utcnow().timestamp():
        raise TokenExpiredException()
    user_id = payload.get("sub")
    if not user_id:
        raise UserNotExistsException()
    user = await UserService.find_by_id(int(user_id))
    if not user:
        raise UserNotExistsException()
    return user


async def get_current_admin_user(current_user: Users = Depends(get_current_user)):
    # if current_user.role != "admin":
    #     raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return await UserService.find_all()
