from db.db import db
from repositories.methods import MethodsRepository
from repositories.methods_association import MethodsAssociationRepository
from repositories.psyhoterapist import PsychotherapistRepository


def get_psychotherapist_repository() -> PsychotherapistRepository:
    return PsychotherapistRepository(db)


def get_method_association() -> MethodsAssociationRepository:
    return MethodsAssociationRepository(db)


def get_methods_repository() -> MethodsRepository:
    return MethodsRepository(db)
