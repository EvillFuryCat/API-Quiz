from fastapi import FastAPI
from database.database_config import SessionLocal
from database.models import Question
from database.schemas import QuestionOut, QuestionBase
import requests


app = FastAPI(
    title="Quiz"
)

@app.post("/quiz", response_model=QuestionOut)
async def get_quiz_questions(questions_num: QuestionBase) -> QuestionOut:
    db = SessionLocal()

    question = None
    while question is None:
        response = requests.get(f"https://jservice.io/api/random?count={questions_num.questions_num}")
        questions = response.json()
        for q in questions:
            q_record = db.query(Question).filter(Question.question == q['question']).first()
            if q_record is None:
                question = Question(question=q['question'], answer=q['answer'])
                db.add(question)
                db.commit()
                db.refresh(question)
            else:
                continue
    db.close()
    return QuestionOut(**question.__dict__)
