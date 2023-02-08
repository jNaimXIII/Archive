from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr
    password: str


class UserCreate(UserBase):
    pass


# NOTE: cannot inherit from UserBase as attribute cannot be removed
class UserResponse(BaseModel):
    email: EmailStr

    id: int
    created_at: datetime

    class Config:
        orm_mode = True


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True
    # rating: Optional[int] = None


class PostCreate(PostBase):
    pass


class PostUpdate(PostBase):
    pass


class PostResponse(PostBase):
    id: int
    created_at: datetime
    author_id: int
    author: UserResponse

    class Config:
        orm_mode = True


class AuthLogin(BaseModel):
    email: EmailStr
    password: str


class AuthResponse(BaseModel):
    access_token: str

    class Config:
        orm_mode = True


class AccessTokenData(BaseModel):
    user_id: Optional[str] = None


class VoteBase(BaseModel):
    post_id: int


class VoteCreate(VoteBase):
    pass


class VoteResponse(VoteBase):
    created_at: datetime

    class Config:
        orm_mode = True
