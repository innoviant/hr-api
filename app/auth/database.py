from fastapi import Depends
from fastapi_users.db import SQLAlchemyBaseUserTableUUID, SQLAlchemyUserDatabase

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import Base, get_async_session


class User(SQLAlchemyBaseUserTableUUID, Base):
    name = Column(String, nullable=False)


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)
