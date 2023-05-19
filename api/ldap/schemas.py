from pydantic import BaseModel as SCBaseModel




class UsuarioSchemaBase(SCBaseModel):
    email: str

    class Config:
        orm_mode = True


class UsuarioSchemaAll(UsuarioSchemaBase):
    usuario: str
