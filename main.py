#Dependencies
from os import getenv
from dotenv import load_dotenv
from os.path import dirname, isfile, join

# setting enviroment file
_ENV_FILE = join(dirname(__file__), '.env_')
if isfile(_ENV_FILE):
    load_dotenv(dotenv_path=_ENV_FILE)

from fastapi import FastAPI
from config import config
from routes import Routes

app = FastAPI(
    title="FastApi-Redis",
    description="Micro-Service Fast API with Redis",
    version="1.0.0",
    docs_url="/api-docs"
)

app.include_router(Routes)