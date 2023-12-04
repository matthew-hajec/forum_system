from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine, Base


Base.metadata.create_all(bind=engine)

app = FastAPI()


# Database Session Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ======================
# WEBSITE CRUD
# ======================
@app.post('/websites', response_model=schemas.Website)
def create_website(website: schemas.WebsiteCreate, db: Session = Depends(get_db)):
    return crud.create_website(db, website)


@app.get('/websites/{website_id}', response_model=schemas.Website)
def get_website(website_id: int, db: Session = Depends(get_db)):
    result = crud.get_website(db, website_id)
    if result is None:
        raise HTTPException(status_code=404, detail='Website not found')
    return result


@app.put('/websites/{website_id}', response_model=schemas.Website)
def update_website(website_id: int, website: schemas.WebsiteUpdate, db: Session = Depends(get_db)):
    return crud.update_website(db, website_id, website)


@app.delete('/websites/{website_id}')
def delete_website(website_id: int, db: Session = Depends(get_db)):
    return crud.delete_website(db, website_id)


# ======================
# USER CRUD
# ======================
@app.post('/users', response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)


@app.get('/users/{user_id}', response_model=schemas.User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    result = crud.get_user(db, user_id)
    if result is None:
        raise HTTPException(status_code=404, detail='User not found')
    return result

@app.put('/users/{user_id}', response_model=schemas.User)
def update_user(user_id: int, user: schemas.UserUpdate, db: Session = Depends(get_db)):
    return crud.update_user(db, user_id, user)


@app.delete('/users/{user_id}')
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return crud.delete_user(db, user_id)


# ======================
# POST CRUD
# ======================
@app.post('/posts', response_model=schemas.Post)
def create_post(post: schemas.PostCreate, db: Session = Depends(get_db)):
    return crud.create_post(db, post)


@app.get('/posts/{post_id}', response_model=schemas.Post)
def get_post(post_id: int, db: Session = Depends(get_db)):
    result = crud.get_post(db, post_id)
    if result is None:
        raise HTTPException(status_code=404, detail='Post not found')
    return result


@app.put('/posts/{post_id}', response_model=schemas.Post)
def update_post(post_id: int, post: schemas.PostUpdate, db: Session = Depends(get_db)):
    return crud.update_post(db, post_id, post)


@app.delete('/posts/{post_id}')
def delete_post(post_id: int, db: Session = Depends(get_db)):
    return crud.delete_post(db, post_id)