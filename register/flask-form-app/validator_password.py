import re

class PasswordValidator:
    def __init__(self, password: str):
        self.password = password

    def is_valid(self) -> bool:
        if not self.password or len(self.password) < 4:
            return False
        pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_+\-=\[\]{};:\'",.<>/?\\|]).{4,}$'
        return re.match(pattern, self.password) is not None

    def field_name(self) -> str:
        return "password"
