from typing import List

from pyairtable import *
from pydantic import parse_obj_as

from schemas.airtable_schemas import AirtablePsychotherapist


def create_connect_to_air_table():
    air_table = Table()
    return air_table


def get_info_from_air_table():
    connection = create_connect_to_air_table()
    return connection.all()


def air_table_map():
    table_info = get_info_from_air_table()
    table_array: List[AirtablePsychotherapist] = []
    for obj in table_info:
        table_array.append(parse_obj_as(AirtablePsychotherapist, obj))
    return table_array
