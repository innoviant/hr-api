from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import get_async_session
from auth import current_user
from sqlalchemy import select
from auth.schemas import UserRead
from auth.database import User

from .models import *
from .schemas import *

router = APIRouter(
    tags=['employees']
)

@router.post('/add_empl', response_model=EmployeeRead)
async def add_employee(employee: EmployeeCreate,
                       user=Depends(current_user),  # protected
                       db: AsyncSession=Depends(get_async_session)
                       ):
    db_link = Employee(name=employee.name, owner_id=user.id, birthdate=employee.birthdate)
    db.add(db_link)

    await db.commit()
    await db.refresh(db_link)

    return db_link


@router.get('/get_empls', response_model=list[EmployeeRead])
async def get_employees(
                       user=Depends(current_user),  # protected
                       db: AsyncSession=Depends(get_async_session)
                       ):
    return list(map(EmployeeRead.from_orm, (await db.execute(
        select(Employee)
        .filter(Employee.owner_id == user.id)
    )).scalars().all()))


@router.get('/get_users', response_model=list[UserRead])
async def get_users(
                   user=Depends(current_user),  # protected
                   db: AsyncSession=Depends(get_async_session)
                    ):
    return list(map(UserRead.from_orm, (await db.execute(
        select(User)
    )).scalars().all()))


@router.get('/get_current_user', response_model=UserRead)
async def get_current_user(
                   user=Depends(current_user),  # protected
                    ):
    return user
