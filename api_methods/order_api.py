import requests
from urls import CREATE_ORDER_URL

def create_order(ingredients=None, token=None):
    headers={}

    if token:
        headers['Authorization'] = token
    
    data = {'ingredients': ingredients} if ingredients else {}

    return requests.post(CREATE_ORDER_URL, json=data, headers=headers)
