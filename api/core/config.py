""" Configuração geral """
from pydantic import BaseSettings




class Settings(BaseSettings):
    # ROTA BASE
    API_V1_STR: str = '/api/v1'

    class Config:
        case_sensitive = True


settings: Settings = Settings()
