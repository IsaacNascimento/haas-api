""" Configuração ldap """
from pydantic import BaseSettings




class Settings(BaseSettings):
    # LDAP3
    LDAP_HOST = "hepta.com.br"
    LDAP_PORT = 389
    LDAP_SEARCH_BASE = "DC=hepta,DC=com,DC=br"
    LDAP_DOMINIO_LOGIN = "hepta\\"
    LDAP_USE_SSL = False

    class Config:
        case_sensitive = True


settings: Settings = Settings()
