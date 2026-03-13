from beanie import PydanticObjectId
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate
from app.services.security.hash import HashService


class UserService:

    def __init__(self, hash_service: HashService):
        self.hash_service = hash_service

    async def create_user(self, data: UserCreate) -> User:

        existing = await User.find_one({"email": data.email})

        if existing:
            raise ValueError("Email already registered")

        password_hash = self.hash_service.hash_password(data.password)

        user = User(
            name=data.name,
            email=data.email,
            password_hash=password_hash,
        )

        await user.insert()

        return user

    async def get_user(self, user_id: PydanticObjectId) -> User | None:
        return await User.get(user_id)

    async def get_user_by_email(self, email: str) -> User | None:
        return await User.find_one({"email": email})

    async def update_user(
        self, user_id: PydanticObjectId, data: UserUpdate
    ) -> User | None:

        user = await User.get(user_id)

        if not user:
            return None

        update_data = data.model_dump(exclude_unset=True)

        if "password" in update_data:
            update_data["password_hash"] = self.hash_service.hash_password(
                update_data.pop("password")
            )

        await user.set(update_data)

        return user

    async def delete_user(self, user_id: PydanticObjectId) -> bool:

        user = await User.get(user_id)

        if not user:
            return False

        await user.delete()

        return True
