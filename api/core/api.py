from fastapi import APIRouter

from auth import router as auth
from exemplo import router as exemplo




api_router = APIRouter()


api_router.include_router(auth.rota, prefix='/auth', tags=['Auth'])
api_router.include_router(exemplo.rota, prefix='/exemplos', tags=['Exemplos'])
