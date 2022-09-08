import datetime
from typing import List, Optional

from pydantic import BaseModel

from schemas.methods_schemas import Methods, ResponseMethods


class Psychotherapist(BaseModel):
    id: str
    name: str
    photo_url: str
    created_at: datetime.datetime
    updated_at: datetime.datetime


class InputPsychotherapist(BaseModel):
    id: str
    name: str
    photo_url: str
    methods_list: List[str]


class ResponsePsychotherapist(BaseModel):
    id: str
    name: str
    photo_url: str
    methods_list: List[ResponseMethods]


class UpdatePsychotherapist(BaseModel):
    id: str
    name: Optional[str]
    photo_url: Optional[str]
    methods_list: Optional[List[Methods]]
    updated_at: datetime.datetime
