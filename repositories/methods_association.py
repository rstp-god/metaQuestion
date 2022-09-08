from typing import List

from fastapi import HTTPException

from db import association_table
from repositories.base import BaseRepository
from schemas.methods_association_schemas import MethodsAssoc


class MethodsAssociationRepository(BaseRepository):

    async def get_all(self, psycho_id: str) -> List[MethodsAssoc]:
        query = association_table.select().where(association_table.c.psycho_id == psycho_id)
        return await self.db.fetch_all(query)

    async def create(self, new_assoc: MethodsAssoc) -> MethodsAssoc or HTTPException:
        query = association_table.select().where(
            association_table.c.psycho_id == new_assoc.psycho_id
            and association_table.c.method_id == new_assoc.method_id)
        response = await self.db.fetch_one(query)
        if response is None:
            new = MethodsAssoc(
                psycho_id=new_assoc.psycho_id,
                method_id=new_assoc.method_id
            )
            insert_value = {**new.dict()}
            query = association_table.insert().values(**insert_value)
            await self.db.execute(query)
            return new
        return HTTPException(status_code=400, detail='Method Association already created')

    async def delete(self, delete_assoc: MethodsAssoc) -> HTTPException:
        query = association_table.select().where(
            association_table.c.psycho_id == delete_assoc.psycho_id
            and association_table.c.method_id == delete_assoc.method_id)
        response = await self.db.fetch_one(query)
        if response is None:
            return HTTPException(status_code=400, detail='No Method Association')
        return HTTPException(status_code=200, detail='Method Association successfully deleted!')
