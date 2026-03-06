from datetime import datetime

from pydantic import BaseModel, EmailStr, Field


class UserResponse(BaseModel):
    id: int

    name: str
    phone: str

    email: EmailStr

    birth_date: datetime
    registered_at: datetime
