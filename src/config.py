from pydantic_settings import BaseSettings
from enum import Enum


class Environment(str, Enum):
    DEVELOPMENT = "development"
    PRODUCTION = "production"


class Setting(BaseSettings):
    ENVIRONMENT: Environment = Environment.DEVELOPMENT
    LOG_PATH: str = "./storage/logs"
    
    def is_development(self) -> bool:
        return self.ENVIRONMENT == Environment.DEVELOPMENT
    
    def is_production(self) -> bool:
        return self.ENVIRONMENT == Environment.PRODUCTION

    class Config:
        env_file = ".env"

settings = Setting()