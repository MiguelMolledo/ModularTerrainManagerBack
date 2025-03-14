from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional
import datetime


class UserBase(BaseModel):
    name: str


class UserCreate(UserBase):
    name: str
    email: EmailStr
    password: str


class UserInDB(UserBase):
    hashed_password: str
    is_superuser: bool
    created_at: datetime
    updated_at: datetime


class UserOut(UserBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
