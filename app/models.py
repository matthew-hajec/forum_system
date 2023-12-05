from datetime import datetime
from sqlalchemy import ForeignKey
from typing import List
from sqlalchemy.orm import mapped_column, relationship, Mapped
from .database import Base


class Website(Base):
    __tablename__ = 'websites'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    domains: Mapped[List["Domain"]] = relationship(back_populates="website")
    users: Mapped[List["User"]] = relationship(back_populates="website")


class Domain(Base):
    __tablename__ = 'domains'
    id: Mapped[int] = mapped_column(primary_key=True)
    domain: Mapped[str]
    website_id: Mapped[int] = mapped_column(ForeignKey('websites.id'))
    website: Mapped["Website"] = relationship(back_populates="domains")

class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    website_id: Mapped[int] = mapped_column(ForeignKey('websites.id'))
    website: Mapped["Website"] = relationship(back_populates="users")
    posts: Mapped[List["Post"]] = relationship(back_populates="user")


class Post(Base):
    __tablename__ = 'posts'
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    posted_at: Mapped[datetime] = mapped_column(default=datetime.now)
    content: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    user: Mapped["User"] = relationship(back_populates="posts")