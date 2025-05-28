import pytest
import allure
from generators import generate_user_body
from methods.user_methods import UserMethods


@allure.step("Создание пользователя")
@pytest.fixture(scope="class")
def generate_user_data():
    user_body = generate_user_body()
    email = user_body['email']
    password = user_body['password']
    name = user_body['name']
    yield [user_body, email, password, name]
    token = UserMethods.user_token(email, password)
    if token:
        UserMethods.delete_user(token)  #Удаление пользователя после прогона тестов


@allure.step("Создание двух пользователей")
@pytest.fixture
def generate_two_users_data():
    user_body_1 = generate_user_body()
    email_1 = user_body_1['email']
    password_1 = user_body_1['password']
    name_1 = user_body_1['name']

    user_body_2 = generate_user_body()
    email_2 = user_body_2['email']
    password_2 = user_body_2['password']
    name_2 = user_body_2['name']

    UserMethods.create_user(user_body_1)
    UserMethods.create_user(user_body_2)

    yield [
        (user_body_1, email_1, password_1, name_1),
        (user_body_2, email_2, password_2, name_2)
    ]

    token_1 = UserMethods.user_token(email_1, password_1)
    if token_1:
        UserMethods.delete_user(token_1)

    token_2 = UserMethods.user_token(email_2, password_2)
    if token_2:
        UserMethods.delete_user(token_2)
