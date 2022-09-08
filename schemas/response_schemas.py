from typing import Optional, Generic, List, TypeVar

from pydantic import BaseModel
from pydantic.generics import GenericModel

T = TypeVar('T')


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
