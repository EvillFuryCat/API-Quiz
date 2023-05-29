from typing import List
from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session

from database.database_config import get_db
from database.models import Question
from database.schemas import QuestionOut, QuestionBase

import requests


app = FastAPI(title="Quiz")


def get_requests_api(questions_num: int):
    try:
        response = requests.get(f"https://jservice.io/api/random?count={questions_num}")
        response.raise_for_status()

        questions = response.json()

        if len(questions) != questions_num:
            raise ValueError("API returned unexpected number of questions")

        return questions

    except (requests.exceptions.RequestException, ValueError) as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to fetch questions from API",
        ) from e


@app.post("/quiz", response_model=QuestionOut)
async def get_quiz_questions(
    questions_num: QuestionBase, db: Session = Depends(get_db)
) -> QuestionOut:
    question = None
    while question is None:
        questions = get_requests_api(questions_num.questions_num)
        for q in questions:
            qrecord = (
                db.query(Question).filter(Question.question == q["question"]).first()
            )
            if qrecord is None:
                question = Question(question=q["question"], answer=q["answer"])
                db.add(question)
                db.commit()
                db.refresh(question)
            else:
                continue
    return QuestionOut(**question.__dict__)
