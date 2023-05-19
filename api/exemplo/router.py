from fastapi import APIRouter, status, Depends, HTTPException, Response

from exemplo.schemas import ExemploSchemaBase
from auth.dependencies import get_current_user




rota = APIRouter()


fake_DB = {}


# EXEMPLOS
@rota.get('/')
async def exemplos(usuario_logado = Depends(get_current_user)):
    lista = []

    for chave in fake_DB:
        lista.append(fake_DB[chave])

    return lista


# EXEMPLO
@rota.get('/{id}')
async def exemplo(id: int, usuario_logado = Depends(get_current_user)):
    if len(fake_DB) != 0:
        return fake_DB[id]
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Não existe um exemplo com ID {id}!")


# NOVO EXEMPLO
@rota.post('/novo', status_code=status.HTTP_201_CREATED)
async def novo_exemplo(exe: ExemploSchemaBase, usuario_logado = Depends(get_current_user)):
    fake_DB[exe.id] = exe

    return exe


# ALTERAR EXEMPLO
@rota.put('/alterar/{id}', status_code=status.HTTP_202_ACCEPTED)
async def alterar_exemplo(exe: ExemploSchemaBase, id: int, usuario_logado = Depends(get_current_user)):
    for chave in fake_DB:
        if chave == id:
            fake_DB.pop(id)
            fake_DB[id] = exe

            return exe
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Não existe um exemplo com ID {id}!")


# DELETAR EXEMPLO
@rota.delete('/deletar/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def deletar_exemplo(id: int, usuario_logado = Depends(get_current_user)):
    fake_DB.pop(id)

    return Response(status_code=status.HTTP_204_NO_CONTENT)
