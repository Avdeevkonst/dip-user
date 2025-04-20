from fastapi import APIRouter, status

from src.schemas import SignUp
from src.user.services import create_user_service

user = APIRouter(
    prefix="/user",
    tags=["user"],
)


@user.post(
    "/sign-up",
    status_code=status.HTTP_201_CREATED,
)
async def sign_up(
    payload: SignUp,
):
    return await create_user_service(payload)
