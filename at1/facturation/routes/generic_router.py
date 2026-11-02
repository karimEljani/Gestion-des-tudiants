from typing import Optional, Type
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import SQLModel

from db.database import get_session
from services.generic_service import CRUDService


def make_crud_router(
    service: CRUDService,
    prefix: str,
    tag: str,
    model: Type[SQLModel],
    create_schema: Optional[Type[SQLModel]] = None,
    update_schema: Optional[Type[SQLModel]] = None,
    not_found_msg: str = "Ressource introuvable",
) -> APIRouter:
    """
    Fabrique un routeur CRUD complet (POST, GET, GET/{id}, PUT/{id}, DELETE/{id}).
    - create_schema : schéma du corps du POST (par défaut : le modèle)
    - update_schema : schéma du corps du PUT, champs optionnels (par défaut : le modèle)
    """
    create_schema = create_schema or model
    update_schema = update_schema or model
    router = APIRouter(prefix=prefix, tags=[tag])

    # CREATE
    async def create(data, session: AsyncSession = Depends(get_session)):
        return await service.create(session, data)

    create.__annotations__["data"] = create_schema
    router.add_api_route("/", create, methods=["POST"], response_model=model)

    # READ ALL
    async def read_all(session: AsyncSession = Depends(get_session)):
        return await service.get_all(session)

    router.add_api_route("/", read_all, methods=["GET"], response_model=list[model])

    # READ ONE
    async def read_one(id_value: int, session: AsyncSession = Depends(get_session)):
        obj = await service.get_one(session, id_value)
        if not obj:
            raise HTTPException(status_code=404, detail=not_found_msg)
        return obj

    router.add_api_route("/{id_value}", read_one, methods=["GET"], response_model=model)

    # UPDATE
    async def update(id_value: int, data, session: AsyncSession = Depends(get_session)):
        obj = await service.update(session, id_value, data)
        if not obj:
            raise HTTPException(status_code=404, detail=not_found_msg)
        return obj

    update.__annotations__["data"] = update_schema
    router.add_api_route("/{id_value}", update, methods=["PUT"], response_model=model)

    # DELETE
    async def delete(id_value: int, session: AsyncSession = Depends(get_session)):
        obj = await service.delete(session, id_value)
        if not obj:
            raise HTTPException(status_code=404, detail=not_found_msg)
        return {"message": f"{tag} supprimé(e)"}

    router.add_api_route("/{id_value}", delete, methods=["DELETE"])

    return router
