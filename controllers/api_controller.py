#Dependencies
from os import getenv
from dotenv import load_dotenv
from os.path import dirname, isfile, join

# setting enviroment file
_ENV_FILE = join(dirname(__file__), '.env_')
if isfile(_ENV_FILE):
    load_dotenv(dotenv_path=_ENV_FILE)

from datetime import datetime
from os import getenv
import json
import redis

# Create an instance of the redis
redis_instance = redis.Redis(
    host=getenv('HOST_REDIS'),
    port='6379')

#password='password'


#GET
def get():
    res_cache = redis_instance.get('test_key')

    if (res_cache != None):
        result = json.loads(res_cache)
    else:
        result = {'msg':'Nothing on Cache'}    
    return result 

#POST
def post(body):
    try:
        #Create a new key on redis 
        redis_instance.set('test_key', json.dumps(body)) 

        return body          
    except Exception as e:
        print(e)
        return {'msg':'Bad Request!', 'error': str(e)}
        
#DELETE
def delete(cache_key):
    redis_instance.delete(cache_key)
    return {'msg':'Success!'}

