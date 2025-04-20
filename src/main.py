from contextlib import asynccontextmanager

from fastapi import APIRouter, FastAPI
from faststream.kafka import KafkaBroker

from src.gateway.routers import gate as gateway_router
from src.user.routers import user as user_router

broker = KafkaBroker("kafka:9092")


@asynccontextmanager
async def lifespan(app: FastAPI):
    await broker.start()
    yield
    await broker.close()


app = FastAPI()

v1_router = APIRouter(prefix="/api/v1")

v1_router.include_router(user_router)
v1_router.include_router(gateway_router)
app.include_router(v1_router)
