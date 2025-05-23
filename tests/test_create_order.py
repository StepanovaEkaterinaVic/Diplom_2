import allure
import generators

from methods.order_methods import OrderMethods
from methods.user_methods import UserMethods


class TestCreateOrder:
    @allure.title('Проверка успешного создания заказа авторизованным пользователем')
    @allure.description('Проверка кода ответа и тела ответа')
    def test_create_order_auth_user(self, generate_user_data):
        UserMethods.create_user(generate_user_data[0])
        access_token = UserMethods.user_token(generate_user_data[1], generate_user_data[2])
        order = OrderMethods.create_order(access_token, {"ingredients": generators.generate_order_body()})
        assert order.status_code == 200
        assert order.json().get("success") is True

    @allure.title('Проверка создания заказа не авторизованным пользователем')
    @allure.description('Проверка кода ответа и тела ответа')
    def test_create_order_without_auth(self):
        order = OrderMethods.create_order(None, {"ingredients": generators.generate_order_body()})
        assert order.status_code == 200
        assert order.json().get("success") is True

    @allure.title('Проверка получения ошибки при создании заказа без ингредиентов зарегистрированным пользователем')
    @allure.description('Проверка кода ответа и тела ответа')
    def test_create_order_auth_user_without_ingredient(self, generate_user_data):
        UserMethods.create_user(generate_user_data[0])
        access_token = UserMethods.user_token(generate_user_data[1], generate_user_data[2])
        order = OrderMethods.create_order(access_token, {"ingredients": None})
        assert order.status_code == 400
        assert order.json().get("success") is False
        assert order.json().get("message") == 'Ingredient ids must be provided'

    @allure.title('Проверка получения ошибки при создании заказа с неверным хэшем зарегистрированным пользователем')
    @allure.description('Проверка кода ответа и тела ответа')
    def test_create_order_auth_user_without_ingredient(self, generate_user_data):
        UserMethods.create_user(generate_user_data[0])
        access_token = UserMethods.user_token(generate_user_data[1], generate_user_data[2])
        order = OrderMethods.create_order(access_token, {"ingredients": generators.generate_invalid_hash()})
        assert order.status_code == 400
        assert order.json().get("success") is False
        assert order.json().get("message") == 'Ingredient ids must be provided'

