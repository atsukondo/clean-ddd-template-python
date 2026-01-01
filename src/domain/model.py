from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, EmailStr


class User(BaseModel):
    """ユーザーの基本情報を表すドメインモデル"""
    
    id: Optional[int] = Field(None, description="ユーザーID")
    name: str = Field(..., min_length=1, max_length=100, description="ユーザー名")
    email: EmailStr = Field(..., description="メールアドレス")
    age: Optional[int] = Field(None, ge=0, le=150, description="年齢")
    is_active: bool = Field(default=True, description="有効フラグ")
    created_at: datetime = Field(default_factory=datetime.now, description="作成日時")
    updated_at: Optional[datetime] = Field(None, description="更新日時")
