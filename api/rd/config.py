""" Configuração geral """
from pydantic import BaseSettings




class Settings(BaseSettings):
    # REDIS 
    REDIS_URL: str = 'redis://localhost:6379'

    class Config:
        case_sensitive = True


settings: Settings = Settings()
