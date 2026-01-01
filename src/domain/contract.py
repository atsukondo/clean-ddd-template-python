from abc import ABC, abstractmethod
from typing import List, Optional
from domain.model import User


class UserRepository(ABC):
    """ユーザーのリポジトリインターフェース"""
    
    @abstractmethod
    async def create(self, user: User) -> User:
        """
        ユーザーを作成し、保存します。
        
        Args:
            user: 作成するユーザー
        
        Returns:
            保存されたユーザー
        """
        pass
    
    @abstractmethod
    async def get_by_id(self, user_id: int) -> Optional[User]:
        """
        IDでユーザーを取得します。
        
        Args:
            user_id: ユーザーID
        
        Returns:
            見つかったユーザー、見つからない場合はNone
        """
        pass
    
    @abstractmethod
    async def get_all(self) -> List[User]:
        """
        全ユーザーを取得します。
        
        Returns:
            ユーザーのリスト
        """
        pass
    
    @abstractmethod
    async def update(self, user_id: int, user: User) -> Optional[User]:
        """
        ユーザーを更新します。
        
        Args:
            user_id: ユーザーID
            user: 更新内容
        
        Returns:
            更新されたユーザー、見つからない場合はNone
        """
        pass
    
    @abstractmethod
    async def delete(self, user_id: int) -> bool:
        """
        ユーザーを削除します。
        
        Args:
            user_id: ユーザーID
        
        Returns:
            削除成功時はTrue、ユーザーが見つからない場合はFalse
        """
        pass
