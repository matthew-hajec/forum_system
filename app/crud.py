from sqlalchemy import select
from sqlalchemy.orm import Session
from . import models, schemas
from sqlalchemy.orm.exc import NoResultFound


# ======================
# WEBSITE CRUD
# ======================
def create_website(session: Session, website: schemas.WebsiteCreate) -> models.Website:
    website = models.Website(**website.model_dump())
    session.add(website)
    session.commit()
    session.refresh(website)
    return website


def get_website(session: Session, website_id: int) -> models.Website:
    try:
        stmt = select(models.Website).where(models.Website.id == website_id)
        result = session.execute(stmt).scalar_one()
        return result
    except NoResultFound:
        return None


def update_website(session: Session, website_id: int, website: schemas.WebsiteUpdate) -> models.Website:
    stmt = select(models.Website).where(models.Website.id == website_id)
    result = session.execute(stmt).scalar_one()
    for key, value in website.model_dump(exclude_unset=True).items():
        setattr(result, key, value)
    session.commit()
    session.refresh(result)
    return result


def delete_website(session: Session, website_id: int) -> None:
    stmt = select(models.Website).where(models.Website.id == website_id)
    result = session.execute(stmt).scalar_one()
    session.delete(result)
    session.commit()


# ======================
# USER CRUD
# ======================
def create_user(session: Session, user: schemas.UserCreate) -> models.User:
    user = models.User(**user.model_dump())
    session.add(user)
    session.commit()
    session.refresh(user)
    return user


def get_user(session: Session, user_id: int) -> models.User:
    try:
        stmt = select(models.User).where(models.User.id == user_id)
        result = session.execute(stmt).scalar_one()
        return result
    except NoResultFound:
        return None


def update_user(session: Session, user_id: int, user: schemas.UserUpdate) -> models.User:
    stmt = select(models.User).where(models.User.id == user_id)
    result = session.execute(stmt).scalar_one()
    for key, value in user.model_dump(exclude_unset=True).items():
        setattr(result, key, value)
    session.commit()
    session.refresh(result)
    return result


def delete_user(session: Session, user_id: int) -> None:
    stmt = select(models.User).where(models.User.id == user_id)
    result = session.execute(stmt).scalar_one()
    session.delete(result)
    session.commit()


# ======================
# POST CRUD
# ======================
def create_post(session: Session, post: schemas.PostCreate) -> models.Post:
    post = models.Post(**post.model_dump())
    session.add(post)
    session.commit()
    session.refresh(post)
    return post


def get_post(session: Session, post_id: int) -> models.Post:
    try:
        stmt = select(models.Post).where(models.Post.id == post_id)
        result = session.execute(stmt).scalar_one()
        return result
    except NoResultFound:
        return None


def update_post(session: Session, post_id: int, post: schemas.PostUpdate) -> models.Post:
    stmt = select(models.Post).where(models.Post.id == post_id)
    result = session.execute(stmt).scalar_one()
    for key, value in post.model_dump(exclude_unset=True).items():
        setattr(result, key, value)
    session.commit()
    session.refresh(result)
    return result


def delete_post(session: Session, post_id: int) -> None:
    stmt = select(models.Post).where(models.Post.id == post_id)
    result = session.execute(stmt).scalar_one()
    session.delete(result)
    session.commit()