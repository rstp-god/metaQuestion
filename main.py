from fastapi import FastAPI
from endpoints import psychoterapist
from airtablescan import air_table_map
from db.db import db

app = FastAPI(title="Meta psychotherapists")
app.include_router(psychoterapist.router, prefix="/psychotherapists", tags=["psychotherapists"])


@app.on_event("startup")
async def startup():
    await db.connect()


@app.on_event("shutdown")
async def shutdown():
    await db.disconnect()


@app.get("/sync")
def sync():
    new_table = air_table_map()
    list_names = []
    list_methods = []
    for i in new_table:
        list_names.append(i.fields.name)
        list_methods.append(i.fields.methods)
    return {"names": list_names, "methods": list_methods}
