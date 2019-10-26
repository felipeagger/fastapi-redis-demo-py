# fastapi-redis-demo-py
Demo Using Fast API with Redis on Python

Salvando e Recuperando dados do Cache no Redis com Python.

# Subir a Aplicacao com Docker:
  Acesse a raiz do repositorio e rode: 
  
```  
  make docker  
```

  Parar a Aplicacao: make dockerdown  

  Para mais detalhes: make help  

# Dependencias

FastAPI, redis, pytest, starlette

# Requisitos :

Deixar as Porta (8000, 6379) do seu host local livre, pois serão essas portas que a aplicacão ira utilizar.

# Fluxo de Inicialização da Aplicacao

 1. Baixa as images da DockerHub;
 2. Docker Faz o Build da Imagem do Python com o Fonte da Aplicacao;
 3. Docker-Compose sobe uma stack com os Containers necessario da API;
 
# Endereços e Servicos

No Navegador acesse: 

API = http://127.0.0.1:8000/api-docs

# Links/Observações

Para Utilizar Docker é necessario ter instalado:

```  
  Docker: https://www.docker.com/

  Docker-Compose: https://docs.docker.com/compose/
  
```  

# Referencias

https://fastapi.tiangolo.com/tutorial/first-steps/

https://redislabs.com/lp/python-redis/