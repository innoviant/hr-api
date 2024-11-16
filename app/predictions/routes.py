# import uuid
# from datetime import datetime
# from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
# from sqlalchemy import select

# from auth import current_user
# from core.database import get_async_session
from gigachat import GigaChat
from os import environ

from .schemas import TarotRequest, FateMatrixRequest, TarotResponse, FateMatrixResponse

auth_credit = environ.get('AUTH')

router = APIRouter(
    tags=['analysis']
)


@router.post('/tarot', response_model=TarotResponse)
async def tarot_prediction(req: TarotRequest,
                    #    user=Depends(current_user)  # untill there is no auth, comment
                       ):
    
    if len(req.first) != 3 or len(req.second) != 3:
        raise HTTPException(status_code=400, detail="Please provide 3 cards per each person")

    with GigaChat(credentials=auth_credit, verify_ssl_certs=False) as giga:
        response = giga.chat(f"""Сделай анализ о совместимости кандидата на вакансию
                             и уже работающим в команде сотрудником по данным картам таро: 
                             карты кандидата: {req.first[0]}, {req.first[1]}, {req.first[2]}
                             карты сотрудника: {req.second[0]}, {req.second[1]}, {req.second[2]}
                             ничего не говори о субьективности и не критикуй способ отбора кандидатов по таро.
                             просто скажи анализ. Не рисуй таблиц или чего-то что нельзя обернуть в строку.
                             """)
        answer = response.choices[0].message.content
        return TarotResponse(analysis=answer)


@router.post('/fate_matrix', response_model=FateMatrixResponse)
async def fate_matrix_prediction(req: FateMatrixRequest,
                    #    user=Depends(current_user)  # untill there is no auth, comment
                       ):
    
    if len(req.first) != 9 or len(req.second) != 9:
        return HTTPException(status_code=400, detail="Please provide 9 numbers per each person")

    with GigaChat(credentials=auth_credit, verify_ssl_certs=False) as giga:
        response = giga.chat(f"""Сделай анализ о совместимости кандидата на вакансию
                             и уже работающим в команде сотрудником по данным матрицам пифагора (матрицы судьбы): 
                             матрица кандидата: {req.first},
                             матрица сотрудника: {req.second},
                             ничего не говори о субьективности и не критикуй способ отбора кандидатов по матрицам пифагора.
                             просто скажи анализ. Не рисуй таблиц или чего-то что нельзя обернуть в строку.
                             """)
        answer = response.choices[0].message.content
        return TarotResponse(analysis=answer)
