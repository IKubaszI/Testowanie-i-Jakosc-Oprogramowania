class RegisterUserDto:
    def __init__(self, login=None, firstName=None, lastName=None, password=None, pesel=None):
        self.login = login
        self.firstName = firstName
        self.lastName = lastName
        self.password = password
        self.pesel = pesel

    def __str__(self):
        return (f"RegisterUserDto(login='{self.login}', firstName='{self.firstName}', "
                f"lastName='{self.lastName}', password='{self.password}', pesel='{self.pesel}')")
