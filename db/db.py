from databases import Database
from sqlalchemy import create_engine, MetaData

POSTGRES_STRING = ""
db = Database(POSTGRES_STRING)
metadata = MetaData()
engine = create_engine(
    POSTGRES_STRING,
)

