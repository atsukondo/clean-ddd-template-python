from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, EmailStr


class UserCreate(BaseModel):
    """ユーザー作成時のリクエストモデル"""
    
    name: str = Field(..., min_length=1, max_length=100, description="ユーザー名")
    email: EmailStr = Field(..., description="メールアドレス")
    age: Optional[int] = Field(None, ge=0, le=150, description="年齢")

    class Config:
        json_schema_extra = {
            "example": {
                "name": "田中太郎",
                "email": "tanaka@example.com",
                "age": 30
            }
        }


class UserUpdate(BaseModel):
    """ユーザー更新時のリクエストモデル"""
    
    name: Optional[str] = Field(None, min_length=1, max_length=100, description="ユーザー名")
    email: Optional[EmailStr] = Field(None, description="メールアドレス")
    age: Optional[int] = Field(None, ge=0, le=150, description="年齢")
    is_active: Optional[bool] = Field(None, description="有効フラグ")

    class Config:
        json_schema_extra = {
            "example": {
                "name": "田中太郎",
                "email": "tanaka@example.com",
                "age": 30,
                "is_active": True
            }
        }


class UserResponse(BaseModel):
    """ユーザー取得時のレスポンスモデル"""
    
    id: int = Field(..., description="ユーザーID")
    name: str = Field(..., description="ユーザー名")
    email: EmailStr = Field(..., description="メールアドレス")
    age: Optional[int] = Field(None, description="年齢")
    is_active: bool = Field(..., description="有効フラグ")
    created_at: datetime = Field(..., description="作成日時")
    updated_at: Optional[datetime] = Field(None, description="更新日時")

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": 1,
                "name": "田中太郎",
                "email": "tanaka@example.com",
                "age": 30,
                "is_active": True,
                "created_at": "2024-01-01T00:00:00",
                "updated_at": None
            }
        }
