from contextlib import asynccontextmanager

from fastapi import APIRouter, FastAPI

from src.services.kafka import broker
from src.user.routers import user as user_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await broker.connect()
    yield
    await broker.close()


app = FastAPI(lifespan=lifespan)

v1_router = APIRouter(prefix="/api/v1")

v1_router.include_router(user_router)
app.include_router(v1_router)
