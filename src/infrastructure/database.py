from typing import List, Optional

from domain.contract import UserRepository
from domain.model import User


class SpecificDatabase(UserRepository):
    """特定のデータベース実装のユーザーリポジトリ"""
    
    async def create(self, user: User) -> User:
        # データベースにユーザーを保存するロジックを実装
        pass
    
    async def get_by_id(self, user_id: int) -> Optional[User]:
        # IDでユーザーを取得するロジックを実装
        pass
    
    async def get_all(self) -> List[User]:
        # 全ユーザーを取得するロジックを実装
        pass
    
    async def update(self, user_id: int, user: User) -> Optional[User]:
        # ユーザーを更新するロジックを実装
        pass
    
    async def delete(self, user_id: int) -> bool:
        # ユーザーを削除するロジックを実装
        pass