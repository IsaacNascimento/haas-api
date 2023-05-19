from pydantic import BaseModel as SCBaseModel
from datetime import date




class ExemploSchemaBase(SCBaseModel):
    id: int
    nome: str
    status: bool
    data: date = date.today()

    class Config:
        orm_mode = True
