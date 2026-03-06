from datetime import datetime

from pydantic import BaseModel


class PostResponse(BaseModel):
    id: int

    title: str
    content: str
    writed_at: datetime

    published: bool
    published_at: datetime | None

    author_id: int
