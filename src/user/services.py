from src.config import settings
from src.database.common import PgUnitOfWork
from src.schemas import SignUp
from src.user.cruds import UserCrud

db_url_postgresql = settings.db_url_postgresql


async def create_user_service(payload: SignUp):
    async with PgUnitOfWork(db_url_postgresql) as uow:
        return await UserCrud(uow=uow).create_user(payload.user)
