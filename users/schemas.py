from pydantic import BaseModel, EmailStr


class SUserAuth(BaseModel):
    email: EmailStr
    hashed_password: str


class SUserAuthDB(BaseModel):
    id: int
    email: EmailStr
    hashed_password: str
