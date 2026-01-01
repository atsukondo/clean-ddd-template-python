from fastapi import APIRouter, HTTPException, status
from typing import List
from datetime import datetime

from application.schemas import (
    UserCreate as UserCreateSchema,
    UserUpdate as UserUpdateSchema,
    UserResponse as UserResponseSchema
)
from domain.model import User
from domain.usecase import (
    UserCreate,
    UserListRetrieve,
    UserRetreive,
    UserUpdate,
    UserDelete
)
from infrastructure.database import SpecificDatabase
from utils import logger


router = APIRouter()


@router.post(
    "/",
    response_model=UserResponseSchema,
    status_code=status.HTTP_201_CREATED
)
async def create_user(user_data: UserCreateSchema) -> UserResponseSchema:    
    logger.debug(f"ユーザー作成リクエスト: {user_data.name}")
    
    user = User(
        name=user_data.name,
        email=user_data.email,
        age=user_data.age,
        created_at=datetime.now()
    )

    usecase = UserCreate(
        user_repository=SpecificDatabase(),
        user=user
    )
    user = await usecase.execute()
    
    logger.info(f"ユーザーを作成しました: ID={user.id}, 名前={user.name}")
    
    return UserResponseSchema.model_validate(user)


@router.get("/", response_model=List[UserResponseSchema])
async def get_all_users() -> List[UserResponseSchema]:
    """全ユーザーを取得します。"""

    usecase = UserListRetrieve(
        user_repository=SpecificDatabase()
    )
    users = await usecase.execute()

    return [UserResponseSchema.model_validate(user) for user in users]


@router.get("/{user_id}", response_model=UserResponseSchema)
async def get_user(user_id: int) -> UserResponseSchema:
    """特定のユーザーを取得します。"""

    logger.debug(f"ユーザー取得: ID={user_id}")
    
    usecase = UserRetreive(
        user_repository=SpecificDatabase(),
        user_id=user_id
    )
    user = await usecase.execute()
    
    return UserResponseSchema.model_validate(user)


@router.put("/{user_id}", response_model=UserResponseSchema)
async def update_user(user_id: int, user_data: UserUpdateSchema) -> UserResponseSchema:
    """ユーザー情報を更新します。"""

    logger.debug(f"ユーザー更新: ID={user_id}")
    
    usecase = UserUpdate(
        user_repository=SpecificDatabase(),
        user_id=user_id
    )
    user = await usecase.execute()
    
    user.updated_at = datetime.now()
    
    logger.info(f"ユーザーを更新しました: ID={user_id}")
    
    return UserResponseSchema.model_validate(user)


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int) -> None:
    """
    ユーザーを削除します。
    
    - **user_id**: ユーザーID（必須）
    """
    logger.debug(f"ユーザー削除: ID={user_id}")
    
    usecase = UserDelete(
        user_repository=SpecificDatabase(),
        user_id=user_id
    )
    await usecase.execute()
    
    logger.info(f"ユーザーを削除しました: ID={user_id}")
