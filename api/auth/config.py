""" Configuração auth """
from pydantic import BaseSettings




class Settings(BaseSettings):
    # JWT
    ACCESS_TOKEN_SECRET: str = 'M3tElo4abm5fidDjKyNb6AyobEu-2NeAnElvS4XCqP0'
    REFRESH_TOKEN_SECRET: str = 'pcwTTSq5MiTFiJivS1s2boc4nPx2dwTq6pUTo7CF9t0'
    ALGORITHM: str = 'HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60    # 1 hora
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 60 * 2  # 2 horas

    class Config:
        case_sensitive = True


settings: Settings = Settings()
