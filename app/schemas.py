from datetime import datetime
from pydantic import BaseModel


class DBModelMixin:
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
        from_attributes = True


class WebsiteBase(BaseModel):
    name: str
    domains: str


class WebsiteCreate(WebsiteBase):
    pass


class WebsiteUpdate(WebsiteBase):
    pass


class Website(WebsiteBase, DBModelMixin):
    pass

class UserBase(BaseModel):
    name: str
    website_id: int


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    pass


class User(UserBase, DBModelMixin):
    pass


class PostBase(BaseModel):
    title: str
    content: str
    user_id: int


class PostCreate(PostBase):
    pass


class PostUpdate(PostBase):
    pass


class Post(PostBase, DBModelMixin):
    pass