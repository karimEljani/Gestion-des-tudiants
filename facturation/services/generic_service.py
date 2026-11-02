from typing import Generic, TypeVar, Type, Optional, Sequence
from sqlmodel import SQLModel, select
from sqlalchemy.ext.asyncio import AsyncSession

ModelType = TypeVar("ModelType", bound=SQLModel)
CreateSchemaType = TypeVar("CreateSchemaType", bound=SQLModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=SQLModel)


class CRUDService(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    """
    Service CRUD générique. Chaque service spécifique (client, article, ...)
    est simplement une instance de cette classe paramétrée par son modèle,
    ce qui lui permet de respecter l'interface attendue par make_crud_router.
    """

    def __init__(self, model: Type[ModelType]):
        self.model = model

    async def create(self, session: AsyncSession, data: CreateSchemaType) -> ModelType:
        # model_validate force la validation/conversion des types (ex. "2026-01-01" -> date),
        # que SQLModel ne fait pas dans __init__ pour les modèles table=True.
        obj = self.model.model_validate(data.model_dump())
        session.add(obj)
        await session.commit()
        await session.refresh(obj)
        return obj

    async def get_all(self, session: AsyncSession) -> Sequence[ModelType]:
        result = await session.execute(select(self.model))
        return result.scalars().all()

    async def get_one(self, session: AsyncSession, id_value: int) -> Optional[ModelType]:
        return await session.get(self.model, id_value)

    async def update(
        self, session: AsyncSession, id_value: int, data: UpdateSchemaType
    ) -> Optional[ModelType]:
        obj = await session.get(self.model, id_value)
        if not obj:
            return None
        changes = data.model_dump(exclude_unset=True)
        # Valide les valeurs modifiées (conversion des dates, etc.)
        validated = self.model.model_validate({**obj.model_dump(), **changes})
        for key in changes:
            if key in self.model.model_fields:
                setattr(obj, key, getattr(validated, key))
        session.add(obj)
        await session.commit()
        await session.refresh(obj)
        return obj

    async def delete(self, session: AsyncSession, id_value: int) -> Optional[ModelType]:
        obj = await session.get(self.model, id_value)
        if not obj:
            return None
        await session.delete(obj)
        await session.commit()
        return obj
