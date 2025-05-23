import allure
from methods.user_methods import UserMethods


class TestCreateUser:
    @allure.title('Проверка успешного создания аккаунта пользователя')
    @allure.description('Проверка кода ответа и тела ответа')
    def test_success_create_user(self, generate_user_data):
        response = UserMethods.create_user(generate_user_data[0])
        assert response.status_code == 200
        assert response.json().get("success") is True

    @allure.title('Проверка получения ошибки при создании пользователя, который уже зарегистрирован')
    @allure.description('Проверка кода ответа и тела ответа')
    def test_negative_create_existing_user(self, generate_user_data):
        UserMethods.create_user(generate_user_data[0])
        response = UserMethods.create_user(generate_user_data[0])
        assert response.status_code == 403
        assert response.json().get("success") is False
        assert response.json().get("message") == 'User already exists'

    @allure.title('Проверка получения ошибки при отсутствии name при регистрации пользователя')
    @allure.description('Проверка кода ответа и тела ответа')
    def test_negative_create_user_without_name(self, generate_user_data):
        response = UserMethods.create_user(generate_user_data[:-1])
        assert response.status_code == 403
        assert response.json().get("success") is False
        assert response.json().get("message") == 'Email, password and name are required fields'

    @allure.title('Проверка получения ошибки при отсутствии email при регистрации пользователя')
    @allure.description('Проверка кода ответа и тела ответа')
    def test_negative_create_user_without_email(self, generate_user_data):
        response = UserMethods.create_user([generate_user_data[0], generate_user_data[2:4]])
        assert response.status_code == 403
        assert response.json().get("success") is False
        assert response.json().get("message") == 'Email, password and name are required fields'

    @allure.title('Проверка получения ошибки при отсутствии password при регистрации пользователя')
    @allure.description('Проверка кода ответа и тела ответа')
    def test_negative_create_user_without_password(self, generate_user_data):
        response = UserMethods.create_user([generate_user_data[0:2], generate_user_data[3]])
        assert response.status_code == 403
        assert response.json().get("success") is False
        assert response.json().get("message") == 'Email, password and name are required fields'



