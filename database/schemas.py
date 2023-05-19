from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class QuestionBase(BaseModel):
    questions_num: int


class QuestionOut(BaseModel):
    id: Optional[int] = None
    question: Optional[str] = None
    answer: Optional[str] = None
    created_date: Optional[datetime] = None

    class Config:
        orm_model = True
