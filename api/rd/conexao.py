import redis as rd
from rd.config import settings




# CONEXÃO REDIS-SERVER
redis = rd.from_url(settings.REDIS_URL, decode_responses=True)
