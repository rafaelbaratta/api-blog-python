from datetime import datetime

from sqlalchemy import Boolean, DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    name: Mapped[str] = mapped_column(String(255), nullable=False)
    phone: Mapped[datetime] = mapped_column(DateTime(11), unique=True, nullable=False)

    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)

    birth_date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    registered_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)

    posts: Mapped[list["Posts"]] = relationship(
        back_populates="author", cascade="all, delete-orphan", lazy="selectin", uselist=False
    )
