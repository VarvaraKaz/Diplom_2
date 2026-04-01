import allure
from api_methods.order_api import create_order
from conftest import create_user_fixture
from data import VALID_INGREDIENTS, INVALID_INGREDIENT, STATUS_OK, STATUS_BAD_REQUEST, STATUS_INTERNAL_ERROR, MESSAGE_NO_INGREDIENTS

@allure.epic("Заказы")
@allure.feature("Создание заказа")
@allure.story("Создание заказа авторизованным пользователем")
def test_create_order_with_auth_user(create_user_fixture):
    _, token = create_user_fixture
    with allure.step("Создание заказа с ингредиентами и авторизацией"):
        response = create_order(ingredients=VALID_INGREDIENTS, token=token)

    with allure.step("Проверка успешного создания заказа"):
        assert response.status_code == STATUS_OK
        assert response.json()['success'] is True

@allure.epic("Заказы")
@allure.feature("Создание заказа")
@allure.story("Создание заказа без авторизации")
def test_create_order_without_auth_user():
    with allure.step("Создание заказа без токена авторизации"):
        response = create_order(ingredients=VALID_INGREDIENTS)

    with allure.step("Проверка успешного ответа"):
        assert response.status_code == STATUS_OK
        assert response.json()['success'] is True

@allure.epic("Заказы")
@allure.feature("Создание заказа")
@allure.story("Создание заказа без ингредиентов")
def test_create_order_without_ingredients(create_user_fixture):
    _, token = create_user_fixture
    with allure.step("Создание заказа без ингредиентов"):
        response = create_order(token=token)

    with allure.step("Проверка кода ответа и сообщения об ошибке"):
        assert response.status_code == STATUS_BAD_REQUEST
        assert MESSAGE_NO_INGREDIENTS in response.json()['message']

@allure.epic("Заказы")
@allure.feature("Создание заказа")
@allure.story("Создание заказа с неверными ингредиентами")
def test_create_order_with_invalid_ingredients(create_user_fixture):
    _, token = create_user_fixture
    with allure.step("Создание заказа с невалидным хешем ингредиентов"):
        response = create_order(ingredients=INVALID_INGREDIENT, token=token)

    with allure.step("Проверка кода ответа"):
        assert response.status_code == STATUS_INTERNAL_ERROR