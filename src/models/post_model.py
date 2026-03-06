from datetime import datetime

from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base


class Post(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    title: Mapped[str] = mapped_column(String(100), nullable=False)
    content: Mapped[str] = mapped_column(String(255), nullable=False)
    writed_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)

    published: Mapped[bool] = mapped_column(Boolean, nullable=False)
    published_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)

    author: Mapped["User"] = relationship(back_populates="posts", lazy="selectin")
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
