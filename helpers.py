import random
import string


def generate_user_data():
    email = ''.join(random.choices(string.ascii_lowercase, k=10)) + '@gmail.com'

    return {
        'email': email,
        'password': '123456',
        'name': 'PraktikumTest'
    }