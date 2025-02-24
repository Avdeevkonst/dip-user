from uuid import UUID

from fastapi import HTTPException

from src.database.common import CrudEntity, PgUnitOfWork
from src.schemas import CreateUser, GetUser, UpdateUser
from src.user.models import User


class UserCrud(CrudEntity):
    def __init__(self, uow: PgUnitOfWork):
        super().__init__(uow=uow, model=User)

    async def create_user(self, payload: dict | CreateUser) -> User:
        return await self.create_entity(payload=payload)

    async def update_user(self, payload: UpdateUser, r_id: UUID):
        conditions = GetUser(id=r_id)
        return await self.update_entity(payload=payload, conditions=conditions)

    async def delete_user(self, conditions: GetUser):
        if not conditions.model_dump():
            raise HTTPException(status_code=400, detail="No conditions provided")
        await self.delete_entity(conditions=conditions)

    async def get_user(self, r_id: UUID) -> User:
        return await self.get_entity(r_id=r_id)

    async def get_by_conditions(self, conditions: GetUser) -> User:
        """Get one user by conditions either by id or username
        :param conditions:
        :return: User
        """

        return await self.get_entity_by_conditions(conditions=conditions)
