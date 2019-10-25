#Dependencies
from controllers.api_controller import *
from models.api_model import Item
from fastapi import APIRouter

Routes = APIRouter()

### ---- Routes ---- ###

###  /api  ###
@Routes.get('/api')
def api_get():
    return get()

@Routes.post('/api', status_code=201) #, response_model=Item
def api_post(item: Item):
    item_dict = item.dict()
    return post(item_dict)

@Routes.delete('/api/{cache_key}')
def api_delete(cache_key):
    return delete(cache_key)   