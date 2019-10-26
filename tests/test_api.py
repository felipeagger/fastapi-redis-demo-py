#Dependencies
from fastapi import FastAPI
from starlette.testclient import TestClient
from random import randint
from os.path import dirname, isfile, join, abspath
from dotenv import load_dotenv
import json

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

_ENV_FILE = join(dirname(__file__), '.env_')

if isfile(_ENV_FILE):
    load_dotenv(dotenv_path=_ENV_FILE)

from main import app 

client = TestClient(app)


body = {
    'name': 'Test',
    'msg': 'Description Test'
}

def test_api_Post_response_201():    
    response = client.post('/api', json=body)
    assert response.status_code == 201 


def test_api_Get_response_200(): 
    response = client.get('/api')    
    assert response.status_code == 200    
    assert response.json() == body

def test_api_Delete_response_200(): 
    response = client.delete('/api/test_key')    
    assert response.status_code == 200    
    assert response.json() == {"msg":"Success!"}
