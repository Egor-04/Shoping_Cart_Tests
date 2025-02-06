from unittest import TestCase

from main import ShoppingCart, Product, CommandProcessing


class TestShoppingCart(TestCase):
    def setUp(self):
        self.cart = ShoppingCart()
        self.cart.create_products([Product(0, 'Арбуз', 100), Product(1, 'Мандарин', 200), Product(2, 'Банан', 300)])

    def test_add_product(self):
        product = self.cart.find_product(0)
        self.cart.add_to_cart(product)
        self.assertIn(product, self.cart._ShoppingCart__items)

    def test_remove_product(self):
        product = self.cart.find_product(0)
        self.cart.add_to_cart(product)
        self.cart.remove_product(0)
        self.assertNotIn(product, self.cart._ShoppingCart__items)

    def test_total_cost(self):
        product1 = self.cart.find_product(0)
        product2 = self.cart.find_product(1)
        self.cart.add_to_cart(product1)
        self.cart.add_to_cart(product2)
        self.assertEqual(self.cart.total_cost(), 300)

    def test_empty_cart_cost(self):
        self.cart.remove_product(0)
        self.assertEqual(self.cart.total_cost(), 0)

    def test_list_products(self):
        product = self.cart.find_product(0)
        self.cart.add_to_cart(product)
        self.assertIn('Арбуз', self.cart.list_products())


'''class TestCommandProcessing(TestCase):
    def setUp(self):
        self.cart = ShoppingCart()
        self.cart.create_products([Product(0, 'Арбуз', 100), Product(1, 'Мандарин', 200), Product(2, 'Банан', 300)])
        self.command_processor = CommandProcessing(self.cart)'''

