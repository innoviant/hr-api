from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Uuid
from sqlalchemy.orm import relationship
from sqlalchemy.types import TIMESTAMP

from core.database import Base


class Employee(Base):
    __tablename__ = 'employees'

    short_id = Column(String, primary_key=True)
    name = Column(String)
    birthdate = Column(type_=TIMESTAMP(timezone=True))
    owner_id = Column(Uuid, ForeignKey('user.id'))

    owner = relationship('user', back_populates='employees')
