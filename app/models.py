from datetime import datetime
from sqlalchemy import ForeignKey
from typing import List
from sqlalchemy.orm import mapped_column, relationship, Mapped
from .database import Base


class Website(Base):
    __tablename__ = 'websites'
    name: Mapped[str]
    domains: Mapped[str]
    users: Mapped[List["User"]] = relationship(back_populates="website")


class User(Base):
    __tablename__ = 'users'
    name: Mapped[str]
    website_id: Mapped[int] = mapped_column(ForeignKey('websites.id'))
    website: Mapped["Website"] = relationship(back_populates="users")
    posts: Mapped[List["Post"]] = relationship(back_populates="user")


class Post(Base):
    __tablename__ = 'posts'
    title: Mapped[str]
    posted_at: Mapped[datetime]
    content: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    user: Mapped["User"] = relationship(back_populates="posts")
