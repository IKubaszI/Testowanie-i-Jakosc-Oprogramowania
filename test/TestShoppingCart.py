import unittest
from src.ShoppingCart import ShoppingCart

class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        print("* setUp")
        self.cart = ShoppingCart()

    def test_add_product(self):
        # Arrange
        product_name = "Apple"
        price = 5
        quantity = 2

        # Act
        result = self.cart.add_product(product_name, price, quantity)

        # Assert
        self.assertTrue(result)
        self.assertIn(product_name, self.cart.get_products())
        print("** test_add_product()")

    def test_add_product_invalid(self):
        # Arrange
        product_name = ""
        price = -1
        quantity = 0

        # Act
        result = self.cart.add_product(product_name, price, quantity)

        # Assert
        self.assertFalse(result)
        print("** test_add_product_invalid()")

    def test_remove_product(self):
        # Arrange
        product_name = "Banana"
        self.cart.add_product(product_name, 3, 1)

        # Act
        result = self.cart.remove_product(product_name)

        # Assert
        self.assertTrue(result)
        self.assertNotIn(product_name, self.cart.get_products())
        print("** test_remove_product()")

    def test_update_quantity(self):
        # Arrange
        product_name = "Orange"
        self.cart.add_product(product_name, 4, 5)
        new_quantity = 10

        # Act
        result = self.cart.update_quantity(product_name, new_quantity)

        # Assert
        self.assertTrue(result)
        self.assertEqual(self.cart.count_products(), new_quantity)
        print("** test_update_quantity()")

    def test_get_total_price(self):
        # Arrange
        product_name = "Grapes"
        price = 2
        quantity = 5
        self.cart.add_product(product_name, price, quantity)
        expected_total = price * quantity

        # Act
        total_price = self.cart.get_total_price()

        # Assert
        self.assertEqual(total_price, expected_total)
        print("** test_get_total_price()")

    def test_add_two_products_remove_one(self):
        # Arrange
        product_name1 = "Apple"
        price1 = 5
        quantity1 = 2
        product_name2 = "Banana"
        price2 = 3
        quantity2 = 1

        # Act
        self.cart.add_product(product_name1, price1, quantity1)
        self.cart.add_product(product_name2, price2, quantity2)

        # Remove one product
        self.cart.remove_product(product_name1)

        # Assert
        self.assertIn(product_name2, self.cart.get_products())
        self.assertNotIn(product_name1, self.cart.get_products())
        self.assertEqual(self.cart.count_products(), quantity2)
        print("** test_add_two_products_remove_one()")

    def test_add_two_products_and_check_product_count(self):
        # Arrange
        product_name1 = "Apple"
        price1 = 5
        quantity1 = 2
        product_name2 = "Orange"
        price2 = 4
        quantity2 = 3

        # Act
        self.cart.add_product(product_name1, price1, quantity1)
        self.cart.add_product(product_name2, price2, quantity2)

        # Assert
        self.assertEqual(self.cart.count_products(), quantity1 + quantity2)
        print("** test_add_two_products_and_check_product_count()")

    def tearDown(self):
        print("*** tearDown()")
        self.cart = None

if __name__ == "__main__":
    unittest.main()
