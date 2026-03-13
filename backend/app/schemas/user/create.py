from pydantic import Field
from .base import UserBase


class UserCreate(UserBase):
    password: str = Field(..., min_length=8, max_length=128)
