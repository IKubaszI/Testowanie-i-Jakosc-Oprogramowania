class Order:
    def __init__(self, id, items, customer):
        self.id = id
        self.items = items
        self.customer = customer

class OrderValidator:
    def validate(self, order):
        print("walidacja zamowienia")

class OrderSaving:
    def save(self, order):
        print("zapisywanie do bazy")

class EmailService:
    def send_email(self, order):
        print("wysyłanie email")

class OrderProcessor:
    def __init__(self, validator, repository, email_service):
        self.validator = validator
        self.repository = repository
        self.email_service = email_service

    def process_order(self, order):
        self.validator.validate(order)
        self.repository.save(order)
        self.email_service.send_email(order)

order = Order("123", ["Produkt A", "Produkt B"], "Jan Kowalski")
validator = OrderValidator()
repository = OrderSaving()
email_service = EmailService()
processor = OrderProcessor(validator, repository, email_service)
processor.process_order(order)
