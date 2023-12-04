from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

engine = create_engine('sqlite:///forum_system.sqlite3', echo=True)
SessionLocal = sessionmaker(engine)

class Base(DeclarativeBase):
    pass
