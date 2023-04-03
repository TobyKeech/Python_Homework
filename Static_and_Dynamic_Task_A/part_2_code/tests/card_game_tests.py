import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card1 = Card("Hearts", 1)
        self.card2 = Card("Hearts", 7)
        self.card_game = CardGame()

    def test_check_for_ace(self):
        result = self.card_game.check_for_ace(self.card1)
        self.assertTrue(result)

    def test_highest_card(self):
        result = self.card_game.highest_card(self.card1, self.card2)
        self.assertEqual(self.card2, result)
    
    def test_cards_total(self):
        cards = [self.card1, self.card2]
        result = self.card_game.cards_total(cards)
        self.assertEqual("You have a total of 8", result)
