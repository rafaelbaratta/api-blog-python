from pydantic import BaseModel, Field


class PostCreate(BaseModel):
    title: str = Field(..., max_length=100)
    content: str = Field(..., max_length=255)

    published: bool = False

    author: id


class PostUpdate(BaseModel):
    title: str | None = Field(None, max_length=100)
    content: str | None = Field(None, max_length=255)

    published: bool | None = None
