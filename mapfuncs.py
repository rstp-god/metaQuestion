from typing import List

from schemas.methods_schemas import ResponseMethods, Methods
from schemas.psychotherapist_schemas import ResponsePsychotherapist, Psychotherapist


async def generate_psycho_response(total_count: int,
                                   base_response: List[Psychotherapist],
                                   method_assoc_repo,
                                   methods_response: List[Methods],
                                   offset: int = 10):
    psycho_list = []
    for value in base_response:
        assoc = await method_assoc_repo.get_all(value.id)
        for method in assoc:
            value.methods_list.append(ResponseMethods.parse_obj(methods_response.find(method.method_id)))
        psycho_list.append(ResponsePsychotherapist.parse_obj(value))
    response = {"extensions": {"totalCount": total_count, "offset": offset, "page": total_count // offset}, "data": psycho_list}
    return response
