from db.db import metadata, engine
from db.tables import association_table, methods, psychotherapist

metadata.create_all(bind=engine)
