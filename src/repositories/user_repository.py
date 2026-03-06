from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from src.models.user_model import User


class UserRepository:

    def __init__(self, session: AsyncSession):
        self.session = session

    async def save(self, new_user: User) -> User:
        pass

    async def read_all(self, limit: int, offset: int) -> User:
        pass

    async def read_by_id(self, id: int) -> User:
        pass

    async def update(self, id: int, updated_user: dict) -> User:
        pass

    async def delete(self, id: int) -> bool:
        pass
