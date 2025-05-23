import allure
import pytest
from methods.user_methods import UserMethods
from generators import generate_user_body, parametrize_new_values


class TestChangeDataUser:
    @allure.title('Проверка успешного изменения данных зарегистрированного пользователя')
    @allure.description('Проверка кода ответа и тела ответа')
    @pytest.mark.parametrize("field, new_value", parametrize_new_values())
    def test_success_change_user_field(self, generate_user_data, field, new_value):
        UserMethods.create_user(generate_user_data[0])
        access_token = UserMethods.user_token(generate_user_data[1], generate_user_data[2])
        new_body = generate_user_body(field, new_value)
        response = UserMethods.change_data_user(new_body, access_token)
        assert response.status_code == 200
        assert response.json().get("success") is True

    @allure.title('Проверка получения ошибки при изменении почты пользователя на почту, которая уже используется')
    @allure.description('Проверка кода ответа и тела ответа')
    def test_change_email_user_already_exists(self, generate_two_users_data):
        user_data = generate_two_users_data
        user_1 = user_data[0]
        user_2 = user_data[1]
        existing_email = user_1[1]
        token = UserMethods.user_token(user_2[1], user_2[2])
        change_email_data = {"email": existing_email}
        change_response = UserMethods.change_data_user(change_email_data, token)
        assert change_response.status_code == 403
        assert change_response.json().get("success") is False
        assert change_response.json().get("message") == 'User with such email already exists'

    @allure.title('Проверка получения ошибки при данных не зарегистрированного пользователя')
    @allure.description('Проверка кода ответа и тела ответа')
    @pytest.mark.parametrize("field", ["name", "password", "email"])
    def test_change_field_user_not_auth(self, generate_user_data, field):
        UserMethods.create_user(generate_user_data[0])
        change_data = generate_user_body()
        new_value = change_data[field]
        change_response = UserMethods.change_data_user({field: new_value}, None)
        assert change_response.status_code == 401
        assert change_response.json().get("success") is False
        assert change_response.json().get("message") == 'You should be authorised'
