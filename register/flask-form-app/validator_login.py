from validator import Validator
from register_form_fields import RegisterFormFields

class LoginValidator(Validator):
    def __init__(self, login):
        self.login = login
        self.LOGIN_MIN_LENGTH = 4

    def is_valid(self):
        return bool(self.login and len(self.login) >= self.LOGIN_MIN_LENGTH)

    def field_name(self):
        return RegisterFormFields.LOGIN
