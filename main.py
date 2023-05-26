from fastapi import FastAPI
from database.database_config import SessionLocal
from database.models import Question
from database.schemas import QuestionOut, QuestionBase
import requests


app = FastAPI(title="Quiz")


@app.post("/quiz", response_model=QuestionOut)
async def get_quiz_questions(questions_num: QuestionBase) -> QuestionOut:
    with SessionLocal() as db:
        question = None
        while question is None:
            response = requests.get(
                f"https://jservice.io/api/random?count={questions_num.questions_num}"
            )
            questions = response.json()
            for q in questions:
                qrecord = (
                    db.query(Question)
                    .filter(Question.question == q["question"])
                    .first()
                )
                if qrecord is None:
                    question = Question(question=q["question"], answer=q["answer"])
                    db.add(question)
                    db.commit()
                    db.refresh(question)
                else:
                    continue
        return QuestionOut(**question.__dict__)
