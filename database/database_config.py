import os
from typing import Any, Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base


DATABASE_NAME = os.getenv("NAME")
DATABASE_PASSWORD = os.getenv("PASSWORD")
DATABASE_HOST = os.getenv("HOST")
DATABASE_USER = os.getenv("USER")

engine = create_engine(
    f"postgresql+psycopg2://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}/{DATABASE_NAME}"
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


async def get_db() -> Generator[Session, Any, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
