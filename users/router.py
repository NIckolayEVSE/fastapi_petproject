from fastapi import APIRouter, Response, Depends

from exceptions import UserAlreadyExistsException, IncorrectEmailORPasswordException
from users.auth import (
    get_password_hash,
    verify_password,
    authenticate_user,
    create_access_token,
)
from users.dao import UserService
from users.dependencies import get_current_user, get_current_admin_user
from users.models import Users
from users.schemas import SUserAuth

router = APIRouter(
    prefix="/auth",
    tags=["Auth & Пользователи"],
)


@router.post("/register")
async def register_user(user_data: SUserAuth):
    existing_user = await UserService.find_one_or_none(email=user_data.email)
    if existing_user:
        raise UserAlreadyExistsException()

    hashed_password = get_password_hash(user_data.hashed_password)
    await UserService.add(email=user_data.email, hashed_password=hashed_password)


@router.post("/login")
async def login_user(response: Response, user_data: SUserAuth):
    user = await authenticate_user(user_data.email, user_data.hashed_password)
    if not user:
        raise IncorrectEmailORPasswordException()
    access_token = create_access_token({"sub": str(user.id)})
    response.set_cookie("booking_access_token", access_token, httponly=True)
    return access_token


@router.post("/logout")
async def logout_user(response: Response):
    response.delete_cookie("booking_access_token")


@router.get("/me")
async def read_users_me(current_user: Users = Depends(get_current_user)):
    return current_user


@router.get("/all")
async def read_users_me(current_user: Users = Depends(get_current_admin_user)):
    return current_user
