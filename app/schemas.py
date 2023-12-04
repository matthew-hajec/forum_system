from datetime import datetime
from pydantic import BaseModel


class WebsiteBase(BaseModel):
    name: str
    domain: str
    description: str


class WebsiteCreate(WebsiteBase):
    pass


class WebsiteUpdate(WebsiteBase):
    pass


class Website(WebsiteBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class UserBase(BaseModel):
    name: str
    website_id: int


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    pass


class User(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class PostBase(BaseModel):
    title: str
    content: str
    user_id: int


class PostCreate(PostBase):
    pass


class PostUpdate(PostBase):
    pass


class Post(PostBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True