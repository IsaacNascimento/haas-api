from fastapi import APIRouter, status, Depends, HTTPException 
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse

from auth.dependencies import get_current_user, post_refresh_token
from auth.service import autenticar
from auth.service import criar_token_acesso, criar_refresh_token
from rd.conexao import redis




rota = APIRouter()


# POST Login
@rota.post('/login')
async def post_login(form_data:OAuth2PasswordRequestForm = Depends()):

    usuario = await autenticar(email=form_data.username, senha=form_data.password)

    if not usuario:
        # ERRO
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Dados de acesso incorretos')
    else:
        # JSON
        content = {"access_token": criar_token_acesso(sub=usuario.email),
                    "refresh_token": criar_refresh_token(sub=usuario.email)}

        return JSONResponse(content=content)


# POST Refresh
@rota.post('/refresh')
async def post_refresh(usuario: str = Depends(post_refresh_token)):

    if not usuario:
        # ERRO 
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Refresh token inválido!')
    else:
        # JSON
        content = {"access_token": criar_token_acesso(sub=usuario),
                    "refresh_token": criar_refresh_token(sub=usuario)}

        return JSONResponse(content=content, status_code=status.HTTP_200_OK)


# GET Logout
@rota.get('/logout')
async def get_logout(usuario_logado = Depends(get_current_user)):

    # JSON
    content = {"Logout": "Success"}
                            
    # REDIS
    redis.delete(usuario_logado['email'])

    return JSONResponse(content=content, status_code=status.HTTP_200_OK)


# GET Logado
@rota.get('/logado')
async def get_logado(usuario_logado = Depends(get_current_user)):
    
    # JSON
    content = {"email": usuario_logado['email'],
                "usuario": usuario_logado['usuario'],
                "vida_token": usuario_logado['vida_token'],
                "isLoggin": True}

    return JSONResponse(content=content)
