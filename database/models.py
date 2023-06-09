from datetime import datetime
from sqlalchemy import Column, Integer, String, TIMESTAMP
from .database_config import engine, Base


class Question(Base):
    __tablename__ = "question"
    id = Column(Integer, primary_key=True)
    question = Column(String, nullable=False)
    answer = Column(String, nullable=False)
    created_date = Column(TIMESTAMP, default=datetime.utcnow)


Base.metadata.create_all(bind=engine)
