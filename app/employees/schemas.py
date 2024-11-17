from datetime import datetime

from pydantic import BaseModel


class EmployeeBase(BaseModel):
    class Config:
        orm_mode = True
        from_attributes = True


class EmployeeCreate(EmployeeBase):
    name: str
    birthdate: datetime


class EmployeeRead(EmployeeBase):
    name: str
    birthdate: datetime
    ID: int
