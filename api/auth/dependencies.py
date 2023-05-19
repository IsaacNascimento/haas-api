from fastapi import Depends, HTTPException, status
from jose import jwt, JWTError

from auth.service import oauth2_schema
from auth.config import settings
from auth.utils import vida_token
from rd.conexao import redis




async def get_current_user(access_token: str = Depends(oauth2_schema)):
    credential_exception: HTTPException = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail={"mensagem": "Não foi possível autenticar a credencial",
                "isLoggin":False},
        headers={"WWW-Authenticate": "Bearer"}
    )

    try:
        payload = jwt.decode(
            access_token,
            settings.ACCESS_TOKEN_SECRET,
            options={"verify_aud": False}
        )

        type: str = payload.get("type")
        id_usuario: str = payload.get("sub")
        
        if id_usuario is None or type != "access_token":
            # ERRO
            raise credential_exception
        else:
            nome_usuario = redis.lindex(id_usuario, 0)
        
    except JWTError:
        # ERRO
        raise credential_exception

    return {"email": id_usuario,
            "usuario": nome_usuario,
            "vida_token": vida_token(id_usuario, type)}


async def post_refresh_token(refresh_token: str = Depends(oauth2_schema)):
    credential_exception: HTTPException = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail={"mensagem": "Não foi possível autenticar a credencial",
                "isLoggin":False},
        headers={"WWW-Authenticate": "Bearer"}
    )

    try:
        payload = jwt.decode(
            refresh_token,
            settings.REFRESH_TOKEN_SECRET,
            options={"verify_aud": False}
        )

        type: str = payload.get("type")
        usuario: str = payload.get("sub")

        if usuario is None or type != "refresh_token":
            # ERRO
            raise credential_exception
        
    except JWTError:
        # ERRO
        raise credential_exception

    return usuario
