from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

from src.utils import Jam, UserRole, Weather


class FromAttr(BaseModel):
    model_config = ConfigDict(from_attributes=True)


class UserBase(FromAttr):
    login: str = Field(min_length=8, max_length=25)
    password: str = Field(min_length=8, max_length=25)
    username: str = Field(min_length=8, max_length=25)
    role: UserRole
    is_active: bool = True
    is_superuser: bool = False


class CreateUser(UserBase): ...


class SignUp(BaseModel):
    user: CreateUser


class ReturnUser(UserBase):
    id: UUID


class GetUser(FromAttr):
    id: UUID


class UpdateUser(FromAttr):
    hashed_password: str = Field(min_length=8)


class CarCreate(BaseModel):
    """Raw car data from traffic sensors."""

    plate_number: str = Field(..., description="Car plate number")
    road_id: UUID
    model: str = Field(..., description="Car model")
    average_speed: int = Field(..., ge=0, description="Current speed from sensor")


class RoadConditionCreate(FromAttr):
    road_id: UUID
    weather_status: Weather
    jam_status: Jam
    name: str = Field(..., min_length=1, max_length=100)
    description: str = Field(..., min_length=1, max_length=400)


class RoadCreate(FromAttr):
    start: str = Field(..., min_length=1, max_length=255)
    end: str = Field(..., min_length=1, max_length=255)
    length: float
    city: str = Field(..., min_length=1, max_length=255)
    name: str = Field(..., min_length=1, max_length=100)
    street: str = Field(..., min_length=1, max_length=255)
    description: str = Field(..., min_length=1, max_length=400)
