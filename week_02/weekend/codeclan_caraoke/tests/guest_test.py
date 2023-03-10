import unittest
from src.guest import Guest


class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Bruce", 35, 100.00)
        # self.guest2 = Guest("Meg", 28, 50.00)

    def test_guest_has_name(self):
        self.assertEqual("Bruce", self.guest.name)

    def test_guest_has_age(self):
        self.assertEqual(35, self.guest.age)
    
    def test_guest_has_wallet(self):
        self.assertEqual(100.00, self.guest.wallet)
