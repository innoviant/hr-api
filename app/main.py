from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from gigachat import GigaChat
from os import environ

app = FastAPI()
auth_credit = environ.get('AUTH')


origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/healthcheck")
def read_root():
    with GigaChat(credentials=auth_credit, verify_ssl_certs=False) as giga:
        response = giga.chat("Какой сейчас год? Скажи всего одну цифру")
        answer = response.choices[0].message.content
        return {"message": f"Hello, FastAPI! {answer}"}
