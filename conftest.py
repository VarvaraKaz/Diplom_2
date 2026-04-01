import pytest
import random
import string
from api_methods.user_api import create_user, delete_user

def generate_user_data():
    email = ''.join(random.choices(string.ascii_lowercase, k=10)) + '@gmail.com'

    return {
        'email': email,
        'password': '123456',
        'name': 'PraktikumTest'
    }

@pytest.fixture
def create_user_fixture():
    user = generate_user_data()
    response = create_user(user)
    access_token = response.json().get('accessToken')

    yield user, access_token
    if access_token:
        delete_user(access_token)