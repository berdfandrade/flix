from datetime import datetime
from beanie import PydanticObjectId
from .base import UserBase


class UserRead(UserBase):
    id: PydanticObjectId
    created_at: datetime
