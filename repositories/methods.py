import datetime
from typing import List

from fastapi import HTTPException

from db import methods
from repositories.base import BaseRepository
from schemas.methods_schemas import Methods, InputMethod, UpdateMethod


class MethodsRepository(BaseRepository):

    async def count_all(self) -> int:
        query = methods.select()
        return len(await self.db.fetch_all(query))

    async def get_all(self, limit: int = 100, offset: int = 0) -> List[Methods]:
        query = methods.select().limit(limit).offset(offset)
        return await self.db.fetch_all(query)

    async def get_by_id(self, id: str) -> Methods or HTTPException:
        query = methods.select().where(methods.c.id == id).first()
        response = await self.db.fetch_one(query)
        if response is None:
            return HTTPException(status_code=400, detail='No Method by this id')
        return Methods.parse_obj(response)

    async def create(self, new_entity: InputMethod) -> Methods or HTTPException:
        query = methods.select().where(methods.c.id == new_entity.id).first()
        response = self.db.execute(query)
        if response is None:
            new_method = Methods(
                id=new_entity.id,
                method_name=new_entity.method_name,
                created_at=datetime.datetime.utcnow(),
                updated_at=datetime.datetime.utcnow()
            )
            insert_value = {**new_method.dict()}
            query = methods.insert().values(**insert_value)
            await self.db.execute(query)
            return new_method
        return HTTPException(status_code=409, detail='Method already exist')

    async def update(self, update_entity: UpdateMethod) -> Methods or HTTPException:
        query = methods.select().where(methods.c.id == update_entity.id).first()
        response = self.db.execute(query)
        if response is None:
            return HTTPException(status_code=400, detail='No Method by this id')
        up_method = Methods(
            id=update_entity.id,
            method_name=update_entity.method_name,
            updated_at=datetime.datetime.utcnow(),
        )
        insert_value = {**up_method.dict()}
        query = methods.insert().values(**insert_value)
        await self.db.execute(query)
        return up_method

    async def delete(self, id: str) -> HTTPException:
        query = methods.select().where(methods.c.id == id).first()
        response = self.db.execute(query)
        if response is None:
            return HTTPException(status_code=400, detail='No Method by this id')
        return HTTPException(status_code=200, detail='Method successfully deleted!')
