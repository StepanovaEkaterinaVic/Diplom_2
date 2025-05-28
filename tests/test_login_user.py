import allure
import random

from data import Message
from methods.user_methods import UserMethods
from generators import generate_user_body


class TestLoginUser:
    @allure.title('Проверка успешного входа в аккаунт пользователя')
    @allure.description('Проверка кода ответа и тела ответа')
    def test_success_login_user(self, generate_user_data):
        UserMethods.create_user(generate_user_data[0])
        response = UserMethods.login_user(generate_user_data[1], generate_user_data[2])
        assert response.status_code == 200
        assert response.json().get("success") is True

    @allure.title('Проверка получения ошибки при вводе неправильного email при входе в аккаунт пользователя')
    @allure.description('Проверка кода ответа и тела ответа')
    def test_negative_user_wrong_email(self, generate_user_data):
        UserMethods.create_user(generate_user_data[0])
        wrong_email = generate_user_body()
        email_value = wrong_email["email"]
        response = UserMethods.login_user(email_value, generate_user_data[2])
        assert response.status_code == 401
        assert response.json().get("success") is False
        assert response.json().get("message") == Message.INCORRECT_INPUT

    @allure.title('Проверка получения ошибки при вводе неправильного пароля при входе в аккаунт пользователя')
    @allure.description('Проверка кода ответа и тела ответа')
    def test_negative_user_wrong_password(self, generate_user_data):
        UserMethods.create_user(generate_user_data[0])
        response = UserMethods.login_user(generate_user_data[1], str(random.randint(1000, 9999)))
        assert response.status_code == 401
        assert response.json().get("success") is False
        assert response.json().get("message") == Message.INCORRECT_INPUT






