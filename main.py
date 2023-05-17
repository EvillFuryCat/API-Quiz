from fastapi import FastAPI


app = FastAPI(
    title="Quiz"
)

@app.get('/')
def get_hello():
    return "hello"