from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

from src.utils import UserRole


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
