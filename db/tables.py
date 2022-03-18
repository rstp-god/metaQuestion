import datetime
import uuid

import sqlalchemy
from sqlalchemy.dialects.postgresql import UUID

from db import metadata

association_table = sqlalchemy.Table("Methods_association", metadata,
                                     sqlalchemy.Column("user_id", UUID(as_uuid=True), sqlalchemy.ForeignKey('Psychotherapist.id')),
                                     sqlalchemy.Column("method_id", UUID(as_uuid=True), sqlalchemy.ForeignKey('Methods.method_id'))
                                     )

methods = sqlalchemy.Table("Methods", metadata,
                           sqlalchemy.Column("method_id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
                           sqlalchemy.Column("method_name", sqlalchemy.String),
                           sqlalchemy.Column("created_at", sqlalchemy.DateTime, default=datetime.datetime.utcnow),
                           sqlalchemy.Column("updated_at", sqlalchemy.DateTime, default=datetime.datetime.utcnow),
                           )

psychotherapist = sqlalchemy.Table("Psychotherapist", metadata,
                                   sqlalchemy.Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
                                   sqlalchemy.Column("name", sqlalchemy.String),
                                   sqlalchemy.Column("url", sqlalchemy.String),
                                   sqlalchemy.Column("created_at", sqlalchemy.DateTime, default=datetime.datetime.utcnow),
                                   sqlalchemy.Column("updated_at", sqlalchemy.DateTime, default=datetime.datetime.utcnow),
                                   )
