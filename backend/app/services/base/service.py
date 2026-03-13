from typing import TypeVar, Generic, Type, List
from beanie import Document, PydanticObjectId

ModelType = TypeVar("ModelType", bound=Document)


class BaseService(Generic[ModelType]):

    def __init__(self, model: Type[ModelType]):
        self.model = model

    async def get(self, id: PydanticObjectId) -> ModelType | None:
        return await self.model.get(id)

    async def list(self, skip: int = 0, limit: int = 20) -> List[ModelType]:
        return await self.model.find_all().skip(skip).limit(limit).to_list()

    async def create(self, data: dict) -> ModelType:
        obj = self.model(**data)
        await obj.insert()
        return obj

    async def update(self, id: PydanticObjectId, data: dict) -> ModelType | None:

        obj = await self.model.get(id)

        if not obj:
            return None

        await obj.set(data)

        return obj

    async def delete(self, id: PydanticObjectId) -> bool:

        obj = await self.model.get(id)

        if not obj:
            return False

        await obj.delete()

        return True
