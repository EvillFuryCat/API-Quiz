import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


DATABASE_NAME = os.getenv("NAME")
DATABASE_PASSWORD = os.getenv("PASSWORD")
DATABASE_HOST = os.getenv("HOST")
DATABASE_USER = os.getenv("USER")

engine = create_engine(f"postgresql+psycopg2://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}/{DATABASE_NAME}")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
