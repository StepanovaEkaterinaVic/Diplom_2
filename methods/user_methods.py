import requests
import curl


class UserMethods:
    @staticmethod
    def create_user(body):
        return requests.post(curl.URL.CREATE_USER_URL, json=body)

    @staticmethod
    def login_user(email, password):
        params = {'email': email, 'password': password}
        return requests.post(curl.URL.LOGIN_USER_URL, json=params)

    @staticmethod
    def change_data_user(body, access_token):
        return requests.patch(curl.URL.USER_URL, headers={"Authorization": access_token}, json=body)

    @staticmethod
    def get_user_data(body, access_token):
        return requests.get(curl.URL.USER_URL, headers={"Authorization": access_token}, json=body)

    @staticmethod
    def user_token(email, password):
        params = {'email': email, 'password': password}
        response = requests.post(curl.URL.LOGIN_USER_URL, json=params)
        if response.status_code == 200:
            return response.json().get('accessToken')
        return None

    @staticmethod
    def delete_user(access_token):
        return requests.delete(curl.URL.USER_URL, headers={"Authorization": f"Bearer {access_token}"})
