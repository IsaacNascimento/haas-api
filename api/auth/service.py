from pytz import timezone
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer
from jose import jwt

from core.config import settings as api_settings
from auth.config import settings
from auth.utils import vida_token
from ldap.ad import consultar_ad
from rd.conexao import redis




oauth2_schema = OAuth2PasswordBearer(
    # Cria um endpoint para autenticacao

    tokenUrl=f"{api_settings.API_V1_STR}/usuarios/login"
)


async def autenticar(email: str, senha: str):
    usuario = consultar_ad(email, senha)

    if not usuario:
        return None
    else:
        # SALVA NO REDIS
        redis.rpush(f"{email}@hepta.com.br", usuario.usuario)

        return usuario


def _criar_token(tipo_token: str, tempo_vida: timedelta, sub: str, secret: str) -> str:
    payload = {}

    sp = timezone('America/Sao_Paulo')
    exp = datetime.now(tz=sp) + tempo_vida
    iat = datetime.now(tz=sp)

    payload["type"] = tipo_token
    payload["exp"] = exp
    payload["iat"] = iat    
    payload["sub"] = str(sub)

    token = jwt.encode(payload, secret, algorithm=settings.ALGORITHM)

    tamnho_lista = redis.llen(sub)

    if tamnho_lista >= 5:
        """
        SE JÁ TIVER SALVO 1 ACCESS TOKEN E REFRESH TOKEN,
        ELE DELETA PARA ADICIONAR OS NOVOS TOKENS
        """
        while(tamnho_lista > 1):
            redis.rpop(sub)
            tamnho_lista -= 1

    # SALVA NO REDIS
    redis.rpush(sub, token, exp.strftime("%Y-%m-%d %H:%M:%S"))

    return {"token": token,
            "exp": exp.strftime("%Y-%m-%d %H:%M:%S"),
            "vida_token": vida_token(sub, tipo_token)}


def criar_token_acesso(sub: str) -> str:

    return _criar_token(
        tipo_token='access_token',
        tempo_vida=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
        sub=sub,
        secret=settings.ACCESS_TOKEN_SECRET
    )


def criar_refresh_token(sub: str) -> str:

    return _criar_token(
        tipo_token='refresh_token',
        tempo_vida=timedelta(minutes=settings.REFRESH_TOKEN_EXPIRE_MINUTES),
        sub=sub,
        secret=settings.REFRESH_TOKEN_SECRET
    )
