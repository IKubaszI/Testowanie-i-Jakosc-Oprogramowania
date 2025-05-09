class LastNameValidator:
    def __init__(self, last_name: str):
        self.last_name = last_name

    def is_valid(self) -> bool:
        return bool(self.last_name and self.last_name.strip())

    def field_name(self) -> str:
        return "lastName"
