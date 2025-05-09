class ResponseData:
    def __init__(self):
        self.invalid_field_names = []
        self.error_code = 200

    def add_invalid_field_name(self, name):
        self.invalid_field_names.append(name)
        self.error_code = 400

    def add_invalid_field_names(self, fields):
        if fields:
            self.invalid_field_names.extend(fields)
            self.error_code = 400

    def get_error_code(self):
        return self.error_code

    def get_invalid_field_names(self):
        return ",".join(self.invalid_field_names)
