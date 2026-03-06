from datetime import datetime

from pydantic import BaseModel, EmailStr, Field


class UserCreate(BaseModel):
    name: str = Field(..., max_length=255)
    phone: str = Field(..., min_length=10, max_length=11)

    email: EmailStr
    password: str = Field(..., min_length=4, max_length=20)

    birth_date: datetime


class UserUpdate(BaseModel):
    name: str | None = Field(None, max_length=255)
    password: str | None = Field(None, min_length=4, max_length=20)
    phone: str | None = Field(None, min_length=10, max_length=11)
