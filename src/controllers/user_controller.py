from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_db
from src.repositories.user_repository import UserRepository
from src.schemas.user_schema import UserCreate, UserUpdate
from src.services.user_service import UserService
from src.views.user_view import UserResponse

router = APIRouter(prefix="/user", tags=["User"])


def get_user_service(db: AsyncSession = Depends(get_db)) -> UserService:
    repo = UserRepository(db)
    service = UserService(repo)
    return service


@router.post("/", summary="Register user", status_code=status.HTTP_201_CREATED, response_model=UserResponse)
async def post_user(user: UserCreate, service: UserService = Depends(get_user_service)):
    return await service.create_user(user)


@router.get("/", summary="Read all users", status_code=status.HTTP_200_OK, response_model=List[UserResponse])
async def get_all_users(limit: int = 50, offset: int = 0, service: UserService = Depends(get_user_service)):
    return await service.read_all_users(limit, offset)


@router.get("/", summary="Read user by id", status_code=status.HTTP_200_OK, response_model=UserResponse)
async def get_user_by_id(id: int, service: UserService = Depends(get_user_service)):
    return await service.read_user_by_id(id)


@router.patch("/", summary="Update user", status_code=status.HTTP_200_OK, response_model=UserResponse)
async def patch_user(id: int, user: UserUpdate, service: UserService = Depends(get_user_service)):
    return await service.update_user(id, user)


@router.delete("/", summary="Delete user", status_code=status.HTTP_204_NO_CONTENT, response_model=None)
async def delete_user(id: int, service: UserService = Depends(get_user_service)):
    await service.delete_user(id)
