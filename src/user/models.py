import uuid
from datetime import datetime

from sqlalchemy import Enum, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from src.utils import UserRole


class Base(DeclarativeBase): ...


class User(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    login: Mapped[str] = mapped_column(String(length=150), nullable=False, unique=True, index=True)
    username: Mapped[str] = mapped_column(String(length=150), nullable=False)
    password: Mapped[str] = mapped_column(String(length=1024), nullable=False)
    role: Mapped[Enum] = mapped_column(Enum(UserRole), name="roleuser")
    created_at: Mapped[datetime] = mapped_column()
    is_active: Mapped[bool] = mapped_column(default=True)
    is_superuser: Mapped[bool] = mapped_column(default=False)

    def __repr__(self) -> str:
        return f"User(id={self.id}, role={self.role}, created_at={self.created_at})"
