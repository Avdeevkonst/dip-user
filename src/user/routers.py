from fastapi import APIRouter, status

from src.generate_data.car import publish
from src.schemas import CarCreate, RoadConditionCreate, RoadCreate, SignUp
from src.services.kafka import (
    publish_car_data,
    publish_road_condition_data,
    publish_road_data,
)
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


@user.post(
    "/publish",
    status_code=status.HTTP_200_OK,
)
async def publish_data():
    return await publish()


@user.post(
    "/create-car",
    status_code=status.HTTP_201_CREATED,
)
async def create_car(
    payload: CarCreate,
):
    await publish_car_data(payload)
    return {"message": "Car data published"}


@user.post(
    "/create-road-condition",
    status_code=status.HTTP_201_CREATED,
)
async def create_road_condition(
    payload: RoadConditionCreate,
):
    await publish_road_condition_data(payload)
    return {"message": "Road condition data published"}


@user.post(
    "/create-road",
    status_code=status.HTTP_201_CREATED,
)
async def create_road(
    payload: RoadCreate,
):
    await publish_road_data(payload)
    return {"message": "Road data published"}
