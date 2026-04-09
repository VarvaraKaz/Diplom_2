import pytest
from api_methods.user_api import create_user, delete_user
from helpers import generate_user_data

@pytest.fixture
def user_data():
    return generate_user_data()


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


@pytest.fixture
def create_user_fixture(user_cleanup):
    user = generate_user_data()
    response = create_user(user)

    user_cleanup(response)

    access_token = response.json().get('accessToken')

    return user, access_token