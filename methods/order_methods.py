import requests
import curl


class OrderMethods:
    @staticmethod
    def create_order(access_token, body):
        return requests.post(curl.URL.ORDER_URL, headers={"Authorization": access_token}, json=body)

    @staticmethod
    def get_user_orders(access_token):
        return requests.get(curl.URL.ORDER_URL, headers={"Authorization": access_token})
