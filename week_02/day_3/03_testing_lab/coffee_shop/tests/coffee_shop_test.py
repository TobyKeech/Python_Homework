import unittest

from src.coffee_shop import CoffeeShop

class TestCoffeeShop(unittest.TestCase):

    def setUp(self):
        self.coffeeshop = CoffeeShop("Costa", 9.99)

    def test_coffeshop_has_name(self):
            self.assertEqual("Costa", self.coffeeshop.name)

    def test_amount_in_till(self):
            self.assertEqual(9.99, self.coffeeshop.till)

    def test_drinks_list(self):
        self.assertEqual(3, self.coffeeshop.drinks_list())














