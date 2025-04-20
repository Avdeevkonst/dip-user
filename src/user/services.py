from src.config import settings
from src.schemas import SignUp
from src.services.common import PgUnitOfWork
from src.user.cruds import UserCrud

db_url_postgresql = settings.db_url_postgresql


async def create_user_service(payload: SignUp):
    async with PgUnitOfWork(db_url_postgresql) as uow:
        user = await UserCrud(uow=uow).create_user(payload.user)

        await uow.commit()

    return user
