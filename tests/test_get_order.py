import allure
import generators
from data import Message

from methods.order_methods import OrderMethods
from methods.user_methods import UserMethods


class TestGetOrder:
    @allure.title('Проверка успешного получения списка заказов авторизованным пользователем')
    @allure.description('Проверка кода ответа и тела ответа')
    def test_create_order_auth_user(self, generate_user_data):
        UserMethods.create_user(generate_user_data[0])
        access_token = UserMethods.user_token(generate_user_data[1], generate_user_data[2])
        OrderMethods.create_order(access_token, {"ingredients": generators.generate_order_body()})
        orders = OrderMethods.get_user_orders(access_token)
        assert orders.status_code == 200
        assert orders.json().get("success") is True

    @allure.title('Проверка получения ошибки при запросе списка заказов без авторизации')
    @allure.description('Проверка кода ответа и тела ответа')
    def test_create_order_auth_user(self, generate_user_data):
        OrderMethods.create_order(None, {"ingredients": generators.generate_order_body()})
        orders = OrderMethods.get_user_orders(None)
        assert orders.status_code == 401
        assert orders.json().get("success") is False
        assert orders.json().get("message") == Message.NEED_AUTHORIZATION
