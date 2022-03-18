import datetime
from typing import List, Generic, TypeVar, Optional

from pydantic import BaseModel
from pydantic.generics import GenericModel

T = TypeVar('T')


class Methods(BaseModel):
    id: str
    method_name: str
    created_at: datetime.datetime
    updated_at: datetime.datetime


class Psychotherapist(BaseModel):
    id: str
    name: str
    photo_url: str
    methods_list: List[Methods]
    created_at: datetime.datetime
    updated_at: datetime.datetime


class ResponseMethods(BaseModel):
    id: str
    method_name: str
    created_at: Optional[datetime.datetime]
    updated_at: Optional[datetime.datetime]


class ResponsePsychotherapist(BaseModel):
    id: str
    name: str
    photo_url: str
    methods_list: List[Methods]
    created_at: Optional[datetime.datetime]
    updated_at: Optional[datetime.datetime]


class UpdatePsychotherapist(BaseModel):
    id: str
    name: Optional[str]
    photo_url: Optional[str]
    methods_list: Optional[List[Methods]]
    updated_at: datetime.datetime


class Extensions(BaseModel):
    totalCount: Optional[int]
    offset: Optional[int]
    page: Optional[int]


class ListResponse(GenericModel, Generic[T]):
    extensions: Optional[Extensions]
    data: List[T]


class Response(GenericModel, Generic[T]):
    extensions: Optional[Extensions]
    data: T
