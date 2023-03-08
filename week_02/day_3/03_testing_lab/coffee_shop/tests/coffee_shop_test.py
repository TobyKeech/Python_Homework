import unittest

from src.coffee_shop import CoffeeShop
from src.drink import Drink
from src.customer import Customer

class TestCoffeeShop(unittest.TestCase):

    def setUp(self):
        self.tea = Drink("tea", 2)
        self.bob = Customer("Bob", 50, 18)
        self.dave = Customer("Dave", 20, 7)
        self.coffeeshop = CoffeeShop("Costa", 100.00, [self.tea])

    def test_coffeshop_has_name(self):
            self.assertEqual("Costa", self.coffeeshop.name)

    def test_amount_in_till(self):
            self.assertEqual(100.00, self.coffeeshop.till)

    def test_drinks_list(self):
        self.assertEqual(1, self.coffeeshop.drinks_list())

    def test_add_cash_to_till(self):
          self.coffeeshop.add_cash_to_till(50)
          expected = 150.00
          actual = self.coffeeshop.till
          self.assertEqual(expected,actual)

    def test_sell_drink(self):
          self.coffeeshop.sell_drink(self.bob, self.tea)
          self.assertEqual(48, self.bob.wallet)
          self.assertEqual(102, self.coffeeshop.till)
    
    def test_checks_age(self):
          age_check = self.coffeeshop.checks_age(self.bob)
          self.assertEqual(True, age_check)

    def test_checks_age(self):
          age_check = self.coffeeshop.checks_age(self.dave)
          self.assertEqual(False, age_check)





          










