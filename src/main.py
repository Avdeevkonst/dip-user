from fastapi import APIRouter, FastAPI

from src.gateway.routers import gate as gateway_router
from src.user.routers import user as user_router

app = FastAPI()

v1_router = APIRouter(prefix="/api/v1")

v1_router.include_router(user_router)
v1_router.include_router(gateway_router)
app.include_router(v1_router)
