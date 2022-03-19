from ..common import BaseModel


from pydantic import (
    EmailStr
)


class UserCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr


class Password(BaseModel):
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


