# HAAS-API

## REDIS-SERVER (executar no wsl2)

- sudo apt-get update
- sudo apt-get install redis (instalar)
- sudo service redis-server start (iniciar servidor redis)
- sudo service redis-server stop (parar servidor redis)

## AMBIENTE VIRTUAL

- Windows - virtualenv venv (cria)
- Windows - venv\Scripts\Activate (ativa)
- Linux - cd virtualenv (target folder)
- Linux - source (target folder)/bin/activate

## DEPENDÊNCIAS

- pip install -r requirements/base.txt
- Ativar VPN da HEPTA
- Ativar servidor redis

## INICIAR CÓDIGO

- python api/main.py

## ROTAS

### Auth

- POST - http://localhost:8000/api/v1/auth/login
- GET - http://localhost:8000/api/v1/auth/logado
- POST - http://localhost:8000/api/v1/auth/refresh
- GET - http://localhost:8000/api/v1/auth/logout

### Exemplo

- GET - http://localhost:8000/api/v1/exemplos/
- GET - http://localhost:8000/api/v1/exemplos/{id}
- POST - http://localhost:8000/api/v1/exemplos/novo
- PUT - http://localhost:8000/api/v1/exemplos/alterar/{id}
- DELETE - http://localhost:8000/api/v1/exemplos/deletar/{id}

## ESTRUTURA DO PROJETO

```
HAAS-API
├── api
|	├── auth
|	|	├── config.py
|	|	├── dependencies.py
|	|	├── models.py
|	|	├── router.py
|	|	├── service.py
|	|	└── utils.py
|	├── core
|	|	├── api.py
|	|	├── config.py
|	|	├── database.py
|	|	└── models.py
|	├── exemplo
|	|	├── models.py
|	|	├── router.py
|	|	├── schemas.py
|	|	└── utils.py
|	├── ldap
|	|	├── ad.py
|	|	├── config.py
|	|	└── schemas.py
|	├── rd
|	|	├── conexao.py
|	|	└── config.py
|	└── main.py
├── requirements
|	├── base.txt
|	├── dev.txt
|	└── prod.txt
├── .dockerignore
├── .env
├──.gitignore
├── Dockerfile
└── README.md
```
