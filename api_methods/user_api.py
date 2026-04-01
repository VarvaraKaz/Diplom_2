import requests
from urls import CREATE_USER_URL, LOGIN_USER_URL, DELETE_USER_URL

def create_user(user_data):
    return requests.post(CREATE_USER_URL, json=user_data)

def login_user(user_data):
    return requests.post(LOGIN_USER_URL, json=user_data)

def delete_user(token):
    return requests.delete(DELETE_USER_URL, headers={'Authorization': token})
