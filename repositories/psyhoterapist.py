from typing import List

from fastapi import HTTPException

from db import psychotherapist
from schemas.db_schemas import ListResponse, Psychotherapist, Response, UpdatePsychotherapist, ResponsePsychotherapist
from base import BaseRepository


class UserRepository(BaseRepository):

    async def get_all(self, limit: int = 100, offset: int = 0) -> List[Psychotherapist]:
        query = psychotherapist.select().limit(limit).offset(offset)
        return await self.db.fetch_all(query=query)

    async def get_by_id(self, id: int) -> Psychotherapist or HTTPException:
        query = psychotherapist.select().where(psychotherapist.c.id == id).first()
        response = await self.db.fetch_one(query=query)
        if response is None:
            return HTTPException
        return Psychotherapist.parse_obj(response)

    async def create(self, new_entity: Psychotherapist) -> Psychotherapist:
        return

    async def update(self, update_entity: UpdatePsychotherapist) -> Psychotherapist:
        return

    async def delete(self, id: int) -> HTTPException:
        return
