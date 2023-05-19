from fastapi import HTTPException, status
from datetime import datetime

from rd.conexao import redis




def vida_token(sub: str, type: str):
    credential_exception: HTTPException = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail={"mensagem": "Não foi possível autenticar a credencial",
                "isLoggin":False},
        headers={"WWW-Authenticate": "Bearer"}
    )

    if type == 'access_token':
        index = 2
    elif type == 'refresh_token':
        index = 4

    if redis.keys(sub):
        exp = datetime.strptime(redis.lindex(sub, index), "%Y-%m-%d %H:%M:%S")
        atual = datetime.now()
        
        vida = exp - atual

        return str(vida).split('.', 2)[0]
    else:
        raise credential_exception
