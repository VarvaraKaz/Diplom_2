VALID_INGREDIENTS = ['61c0c5a71d1f82001bdaaa72']
INVALID_INGREDIENT = ['wrong_hash']

STATUS_OK = 200
STATUS_CREATED = 200
STATUS_BAD_REQUEST = 400
STATUS_UNAUTHORIZED = 401
STATUS_FORBIDDEN = 403
STATUS_INTERNAL_ERROR = 500

MESSAGE_USER_EXISTS = 'User already exists'
MESSAGE_REQUIRED_FIELDS = 'Email, password and name are required fields'
MESSAGE_LOGIN_ERROR = 'email or password are incorrect'
MESSAGE_NO_INGREDIENTS = 'Ingredient ids must be provided'

CREATE_USER_DATA_WITHOUT_EMAIL = {
    'password': '123456',
    'name': 'Praktikum'
}

CREATE_USER_DATA_WITHOUT_PASSWORD = {
    'email': 'praktikuml123456@gmail.com',
    'name': 'Praktikum'
}

CREATE_USER_DATA_WITHOUT_NAME = {
    'email': 'praktikuml123456@gmail.com',
    'password': '123456'
}

INVALID_USER_DATA = {
    'email': 'wrong@gmail.com',
    'password': 'wrongpassword'
}