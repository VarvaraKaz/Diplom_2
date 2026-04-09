import allure
from api_methods.user_api import login_user
from conftest import generate_user_data
from data import STATUS_OK, STATUS_UNAUTHORIZED, MESSAGE_LOGIN_ERROR, INVALID_USER_DATA

@allure.epic("Пользователи")
@allure.feature("Авторизация")
@allure.story("Авторизация существующего пользователя")
def test_login_existing_user(create_user_fixture):
    user, _ = create_user_fixture
    with allure.step("Вход под существующим пользователем"):
        response = login_user(user)

    with allure.step("Проверка успешного входа"):
        assert response.status_code == STATUS_OK
        assert response.json()['success'] is True

@allure.epic("Пользователи")
@allure.feature("Авторизация")
@allure.story("Попытка авторизации с неверными данными")
def test_login_with_invalid_credentials():
    with allure.step("Отправка запроса с неверным email и паролем"):
        response = login_user(INVALID_USER_DATA)

    with allure.step("Проверка кода ответа и сообщения об ошибке"):
        assert response.status_code == STATUS_UNAUTHORIZED
        assert response.json()['message'] == MESSAGE_LOGIN_ERROR
