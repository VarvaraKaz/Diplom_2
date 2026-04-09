import pytest
import allure
from api_methods.user_api import create_user, delete_user
from conftest import generate_user_data
from data import STATUS_OK, STATUS_FORBIDDEN, MESSAGE_USER_EXISTS, MESSAGE_REQUIRED_FIELDS, CREATE_USER_DATA_WITHOUT_NAME, CREATE_USER_DATA_WITHOUT_EMAIL, CREATE_USER_DATA_WITHOUT_PASSWORD

@allure.epic("Пользователи")
@allure.feature("Создание пользователя")
@allure.story("Создание уникального пользователя")
def test_create_unique_user(user_cleanup):
    user = generate_user_data()
    with allure.step("Отправка запроса на создание нового пользователя"):
        response = create_user(user)

    user_cleanup(response)

    with allure.step("Проверка ответа сервера"):
        assert response.status_code == STATUS_OK
        assert response.json()['success'] is True

@allure.epic("Пользователи")
@allure.feature("Создание пользователя")
@allure.story("Попытка создания уже существующего пользователя")
def test_create_existing_user(create_user_fixture):
    user, _ = create_user_fixture
    with allure.step("Отправка запроса на создание уже существующего пользователя"):
        response = create_user(user)

    with allure.step("Проверка ответа"):
        assert response.status_code == STATUS_FORBIDDEN
        assert response.json()['message'] == MESSAGE_USER_EXISTS

@allure.epic("Пользователи")
@allure.feature("Создание пользователя")
@allure.story("Создание пользователя без обязательного поля")
@pytest.mark.parametrize('user_data', 
                         [CREATE_USER_DATA_WITHOUT_EMAIL, 
                          CREATE_USER_DATA_WITHOUT_PASSWORD,
                          CREATE_USER_DATA_WITHOUT_NAME])

def test_create_user_without_required_field(user_data):
    with allure.step(f"Отправка запроса с пропущенным полем: {user_data}"):
        response = create_user(user_data)

    with allure.step("Проверка кода ответа и сообщения об ошибке"):
        assert response.status_code == STATUS_FORBIDDEN
        assert MESSAGE_REQUIRED_FIELDS in response.json()['message']