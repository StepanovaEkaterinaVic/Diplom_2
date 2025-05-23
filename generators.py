from faker import Faker
import time
import random

from data import DataOrder

fake = Faker()


def generate_user_body(field=None, new_value=None):
    timestamp = int(time.time())
    user_data = {
        "email": f"{fake.user_name()}_{timestamp}@example.com",
        "password": str(fake.random_int(min=1000, max=99999999)),
        "name": fake.first_name()
    }
    if field and new_value:
        user_data[field] = new_value
    return user_data


def generate_new_value(field):
    timestamp = int(time.time())
    if field == "email":
        return f"new_email_{timestamp}@ex.com"
    elif field == "name":
        return f"NewName_{timestamp}_{random.randint(1000, 9999)}"
    elif field == "password":
        return f"newpassword_{timestamp}_{random.randint(1000, 9999)}"
    else:
        raise ValueError(f"Unknown field: {field}")


def parametrize_new_values():
    return [(field, generate_new_value(field)) for field in ["email", "name", "password"]]


def generate_order_body():
    ingredients = list(DataOrder.ingredients_value.values())
    return random.sample(ingredients, 4)


def generate_invalid_hash():
    return fake.random_int(min=1000, max=99999999)
