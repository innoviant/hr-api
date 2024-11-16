from uuid import UUID
from datetime import datetime

from pydantic import BaseModel


class EmployeeBase(BaseModel):
    class Config:
        orm_mode = True
        from_attributes = True


class EmployeeCreate(EmployeeBase):
    name: str
    birth_date: datetime


class EmployeeRead(EmployeeBase):
    name: str
    birth_date: datetime
    ID: int
