class ShoppingCart:
    def __init__(self):
        self.products = {}
        self.discount = 0


    def add_product(self, product_name: str, price: int, quantity: int) -> bool:
        if price < 0 or quantity <= 0:
            return False
        if product_name in self.products:
            return False
        else:
            self.products[product_name] = {'price': price, 'quantity': quantity}
        return True
        """Dodawanie produktu do koszyka"""
        pass

    def remove_product(self, product_name: str) -> bool:
        return self.products.pop(product_name, None) is not None
        """Usuwanie produktu z koszyka"""
        pass

    def update_quantity(self, product_name: str, new_quantity: int) -> bool:
        if new_quantity <= 0 or product_name not in self.products:
            return False
        self.products[product_name]['quantity'] = new_quantity
        return True
        """Aktualizacja iloĹci produktu w koszyku"""
        pass

    def get_products(self):
        return list(self.products.keys())
        """Pobieranie nazw produktĂłw z koszyka"""
        pass

    def count_products(self) -> int:
        return sum(item['quantity'] for item in self.products.values())
        """Pobieranie liczby produktĂłw znajdujÄcych siÄ w koszyku"""
        pass

    def get_total_price(self) -> int:
        total = sum(item['price'] * item['quantity'] for item in self.products.values())
        return int(total * (1 - self.discount))
        """Pobieranie sumy cen produktĂłw w koszyku"""
        pass

    def apply_discount_code(self, discount_code: str) -> bool:
        valid_discounts = {"DISCOUNT10": 0.1, "DISCOUNT20": 0.2}
        if discount_code in valid_discounts:
            self.discount = valid_discounts[discount_code]
            return True
        return False
        """Zastosowanie kuponu rabatowego"""
        pass

    def checkout(self) -> bool:
        if not self.products:
            return False
        self.products.clear()
        self.discount = 0
        return True
        """Realizacja zamĂłwienia"""
        pass