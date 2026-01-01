from abc import ABC, abstractmethod
from dataclasses import dataclass

from domain.contract import UserRepository
from domain.model import User


class UseCase(ABC):
    
    @abstractmethod
    async def execute(self):
        pass
    

@dataclass
class UserCreate(UseCase):
    user_repository: UserRepository
    user: User

    async def execute(self):
        return await self.user_repository.create(self.user)


@dataclass
class UserListRetrieve(UseCase):
    user_repository: UserRepository

    async def execute(self):
        return await self.user_repository.get_all()


@dataclass
class UserRetreive(UseCase):
    user_repository: UserRepository
    user_id: int

    async def execute(self):
        return await self.user_repository.get_by_id(self.user_id)
    

@dataclass
class UserUpdate(UseCase):
    user_repository: UserRepository
    user_id: int
    user: User

    async def execute(self):
        return await self.user_repository.update(self.user_id, self.user)
    

@dataclass
class UserDelete(UseCase):
    user_repository: UserRepository
    user_id: int

    async def execute(self):
        return await self.user_repository.delete(self.user_id)