from uuid import UUID
from datetime import datetime

from pydantic import BaseModel

class TarotRequest(BaseModel):
    first: list[str]
    second: list[str]

class FateMatrixRequest(BaseModel):
    first: list[int]
    second: list[int]

class TarotResponse(BaseModel):
    analysis: str

class FateMatrixResponse(BaseModel):
    analysis: str

class ConclusionRequest(BaseModel):
    tarot: str
    fate_matrix: str

class ConclusionResponse(BaseModel):
    analysis: str
