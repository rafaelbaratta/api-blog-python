from datetime import datetime

from sqlalchemy.exc import IntegrityError

from src.models.user_model import User
from src.schemas.user_schema import UserCreate, UserUpdate


class UserService:

    def __init__(self, repo):
        self.repo = repo

    async def create_user(self, user: UserCreate) -> User:
        new_user = User(
            name=user.name,
            phone=user.phone,
            email=user.email,
            password=user.password,
            birth_date=user.birth_date,
            registered_at=datetime.now(),
        )

        try:
            return await self.repo.save(new_user)
        except IntegrityError as e:
            orig = str(e.orig)
            if "phone" in orig:
                raise "PhoneAlreadyExists"
            elif "email" in orig:
                raise "EmailAlreadyExists"
            else:
                raise

    async def read_all_users(self, limit: int, offset: int) -> User:
        pass

    async def read_user_by_id(self, id: int) -> User:
        pass

    async def update_user(self, id: int, user: UserUpdate) -> User:
        pass

    async def delete_user(self, id: int) -> None:
        pass
