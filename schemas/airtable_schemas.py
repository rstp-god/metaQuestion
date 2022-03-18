from pydantic import BaseModel, Field
from typing import Dict, List


class ImgSizes(BaseModel):
    url: str
    width: int
    height: int


class Photo(BaseModel):
    id: str
    width: int
    height: int
    url: str
    filename: str
    size: int
    type: str
    thumbnails: Dict[str, ImgSizes]


class Attachment(BaseModel):
    photo: List[Photo] = Field(alias='Фотография')
    methods: List[str] = Field(alias='Методы')
    name: str = Field(alias='Имя')


class AirtablePsychotherapist(BaseModel):
    id: str
    fields: Attachment
    createdTime: str