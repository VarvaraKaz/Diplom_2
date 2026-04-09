import pytest
from api_methods.user_api import create_user, delete_user
from helpers import generate_user_data


@pytest.fixture
def user_data():
    return generate_user_data()


@pytest.fixture
def create_user_fixture():
    user = generate_user_data()
    response = create_user(user)
    access_token = response.json().get('accessToken')

    yield user, access_token

    if access_token:
        delete_user(access_token)

@pytest.fixture
def user_cleanup():
    tokens = []

    def register_for_cleanup(response):
        token = response.json().get('accessToken')
        if token:
            tokens.append(token)

    yield register_for_cleanup

    for token in tokens:
        delete_user(token)