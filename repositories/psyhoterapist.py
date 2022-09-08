import datetime
from typing import List

from fastapi import HTTPException
from sqlalchemy.dialects.postgresql import UUID

from db import psychotherapist
from repositories.base import BaseRepository
from schemas.psychotherapist_schemas import Psychotherapist, UpdatePsychotherapist, InputPsychotherapist


class PsychotherapistRepository(BaseRepository):

    async def count_all(self) -> int:
        query = psychotherapist.select()
        return len(await self.db.fetch_all(query))

    async def get_all(self, limit: int = 100, offset: int = 0) -> List[Psychotherapist]:
        query = psychotherapist.select().limit(limit).offset(offset)
        return await self.db.fetch_all(query=query)

    async def get_by_id(self, id: str) -> Psychotherapist or HTTPException:
        query = psychotherapist.select().where(psychotherapist.c.id == id).first()
        response = await self.db.fetch_one(query=query)
        if response is None:
            return HTTPException(status_code=400, detail='No Psychotherapist by this id')
        return Psychotherapist.parse_obj(response)

    async def create(self, new_entity: InputPsychotherapist) -> Psychotherapist:
        new_psycho = Psychotherapist(
            id=new_entity.id,
            name=new_entity.name,
            photo_url=new_entity.photo_url,
            created_at=datetime.datetime.utcnow(),
            updated_at=datetime.datetime.utcnow(),
        )
        insert_value = {**new_psycho.dict()}
        query = psychotherapist.insert().values(**insert_value)
        await self.db.execute(query)
        return new_psycho

    async def update(self, update_entity: UpdatePsychotherapist) -> Psychotherapist or HTTPException:
        query = psychotherapist.select().where(psychotherapist.c.id == update_entity.id).first()
        response = await self.db.fetch_one(query=query)
        if response is None:
            return HTTPException(status_code=400, detail='No Psychotherapist by this id')
        up_psycho = Psychotherapist(
            id=update_entity.id,
            name=update_entity.name,
            photo_url=update_entity.photo_url,
            created_at=datetime.datetime.utcnow(),
            updated_at=datetime.datetime.utcnow(),
        )
        insert_value = {**up_psycho.dict()}
        query = psychotherapist.update().where(psychotherapist.c.id == update_entity.id).values(**insert_value)
        await self.db.execute(query)
        return up_psycho

    async def delete(self, id: str) -> HTTPException:
        query = psychotherapist.select().where(psychotherapist.c.id == id).first()
        response = await self.db.fetch_one(query=query)
        if response is None:
            return HTTPException(status_code=400, detail='No Psychotherapist by this id')
        query = psychotherapist.delete().where(psychotherapist.c.id == id)
        await self.db.execute(query)
        return HTTPException(status_code=200, detail='Psychotherapist successfully deleted!')
