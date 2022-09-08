from pydantic import BaseModel


class MethodsAssoc(BaseModel):
    psycho_id: str
    method_id: str

