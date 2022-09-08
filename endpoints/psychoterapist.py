from fastapi import APIRouter, Depends
from fastapi import HTTPException

from endpoints.depends import get_psychotherapist_repository, get_methods_repository
from mapfuncs import generate_psycho_response
from repositories.methods import MethodsRepository
from repositories.methods_association import MethodsAssociationRepository
from repositories.psyhoterapist import PsychotherapistRepository
from schemas.methods_association_schemas import MethodsAssoc
from schemas.psychotherapist_schemas import ResponsePsychotherapist, InputPsychotherapist
from schemas.response_schemas import ListResponse

router = APIRouter()


@router.get("", response_model=ListResponse[ResponsePsychotherapist])
async def get_all_psychotherapists(
        psychotherapist_repo: PsychotherapistRepository = Depends(get_psychotherapist_repository),
        method_repo: MethodsRepository = Depends(get_methods_repository),
        method_assoc_repo: MethodsAssociationRepository = Depends(get_psychotherapist_repository),
        limit: int = 100,
        offset: int = 10
) -> ListResponse[ResponsePsychotherapist]:
    total_count = await psychotherapist_repo.count_all()
    base_response = await psychotherapist_repo.get_all(limit, offset)
    methods_response = await method_repo.get_all()
    return ListResponse[ResponsePsychotherapist].parse_obj(
        await generate_psycho_response(
            total_count,
            base_response,
            method_assoc_repo,
            methods_response,
            offset)
    )


@router.get("/{id}")
async def get_psychoterapist_by_id(
        id: str,
        psychotherapist_repo: PsychotherapistRepository = Depends(get_psychotherapist_repository),
        method_repo: MethodsRepository = Depends(get_methods_repository),
        method_assoc_repo: MethodsAssociationRepository = Depends(get_psychotherapist_repository),
) -> ResponsePsychotherapist:
    psycho = await psychotherapist_repo.get_by_id(id)
    methods_ids = await method_assoc_repo.get_all(id)
    methods = list()
    for method_id in methods_ids:
        methods.append(await method_repo.get_by_id(method_id.method_id))
    return ResponsePsychotherapist.parse_obj({**psycho.dict(), "methods": methods})
W

@router.post("", response_model=ResponsePsychotherapist)
async def set_new_psychoterapist(
        new_psycho: InputPsychotherapist,
        psychotherapist_repo: PsychotherapistRepository = Depends(get_psychotherapist_repository),
        method_repo: MethodsRepository = Depends(get_methods_repository),
        method_assoc_repo: MethodsAssociationRepository = Depends(get_psychotherapist_repository)
) -> ResponsePsychotherapist or HTTPException:
    methods = await method_repo.get_all()
    if new_psycho.methods_list not in methods:
        return HTTPException(status_code=400, detail='No methods like this!')
    psycho = await psychotherapist_repo.create(new_psycho)
    methods = list()
    for method in new_psycho.methods_list:
        methods.append(await method_assoc_repo.create(MethodsAssoc.parse_obj({"psycho_id": new_psycho.id, "method_id": method})))
    return ResponsePsychotherapist.parse_obj({**psycho.dict(), "methods": methods})


@router.put("/{id}", response_model=ResponsePsychotherapist)
async def update_psychoterapist(
        id: str,
        psychotherapist_repo: PsychotherapistRepository = Depends(get_psychotherapist_repository),
        method_repo: MethodsRepository = Depends(get_methods_repository),
        method_assoc_repo: MethodsAssociationRepository = Depends(get_psychotherapist_repository)
) -> ResponsePsychotherapist:
