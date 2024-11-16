from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from gigachat import GigaChat

from config import APP_META
from auth.routes import *
from predictions.routes import router as prediction_router
from employees.routes import router as employees_router

from os import environ

app = FastAPI(**APP_META)
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

app.include_router(
    auth_router,
    prefix='/auth',
    tags=['auth']
)

app.include_router(
    register_router,
    prefix='/auth',
    tags=['auth']
)

app.include_router(
    verify_router,
    prefix='/auth',
    tags=['auth']
)

app.include_router(
    reset_password_router,
    prefix='/auth',
    tags=['auth']
)

app.include_router(
    prediction_router
)

app.include_router(
    employees_router
)

@app.get("/healthcheck")
def read_root():
    with GigaChat(credentials=auth_credit, verify_ssl_certs=False) as giga:
        response = giga.chat("Какой сейчас год? Скажи всего одну цифру")
        answer = response.choices[0].message.content
        return {"message": f"Hello, FastAPI! {answer}"}
