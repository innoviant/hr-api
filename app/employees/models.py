from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Uuid
from sqlalchemy.orm import relationship
from sqlalchemy.types import TIMESTAMP

from core.database import Base


class Employee(Base):
    __tablename__ = 'employees'

    ID = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    name = Column(String)
    birthdate = Column(type_=TIMESTAMP(timezone=True), nullable=False)
    owner_id = Column(Uuid, ForeignKey('user.id'))

    owner = relationship('User', back_populates='employees')
