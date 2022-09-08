import datetime
from typing import Optional

from pydantic import BaseModel


class Methods(BaseModel):
    id: str
    method_name: str
    created_at: datetime.datetime
    updated_at: datetime.datetime


class InputMethod(BaseModel):
    id: str
    method_name: str


class UpdateMethod(BaseModel):
    id: str
    method_name: str


class ResponseMethods(BaseModel):
    id: str
    method_name: str
