import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# Database Connection
if 'DATABASE_URL' not in os.environ:
    os.environ['DATABASE_URL'] = 'sqlite:///db.sqlite3'

engine = create_engine(os.environ['DATABASE_URL'])
SessionLocal = sessionmaker(engine)

class Base(DeclarativeBase):
    pass
