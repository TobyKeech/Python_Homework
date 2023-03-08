import unittest

from src.coffee_shop import CoffeeShop

class TestCoffeeShop(unittest.TestCase):

    def setUp(self):
        self.coffeeshop = CoffeeShop("Costa", 100.00, 5.00)

    def test_coffeshop_has_name(self):
            self.assertEqual("Costa", self.coffeeshop.name)

    def test_amount_in_till(self):
            self.assertEqual(100.00, self.coffeeshop.till)

    def test_drinks_list(self):
        self.assertEqual(3, self.coffeeshop.drinks_list())

    def test_add_cash_to_till(self):
          self.coffeeshop.add_cash_to_till(50)
          expected = 150.00
          actual = self.coffeeshop.till
          self.assertEqual(expected,actual)
    
    def test_sell_drink_to_customer(self,customer,price):
          customer = ("Bruce", 150.00)
          price = (5.00)

          self.coffeeshop.drinks
          customer.reduce_cash
          self.till.add_cash_to_till


          










