import unittest
from src.guest import Guest


class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest_1= Guest("Bruce", 35, 100.00)
        self.guest_2 = Guest("Meg", 28, 50.00)

    def test_guest_has_name(self):
        self.assertEqual("Bruce", self.guest_1.name)

    def test_guest_has_age(self):
        self.assertEqual(35, self.guest_1.age)
    
    def test_guest_has_wallet(self):
        self.assertEqual(50.00, self.guest_2.wallet)

    def test_guest_can_reduce_wallet(self):
        self.guest_2.reduce_wallet(5)
        self.assertEqual(45.00, self.guest_2.wallet)
