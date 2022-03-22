import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card_game = CardGame()
        self.card1 = Card("hearts", 10)
        self.card2 = Card("diamonds", 2)
        self.card3 = Card("spades", 1)
        self.cards = [self.card1, self.card2, self.card3]

    def test_check_for_ace_true(self):
        false_result = self.card_game.check_for_ace(self.card2)
        true_result = self.card_game.check_for_ace(self.card3)
        self.assertEqual(False, false_result)
        self.assertEqual(True, true_result)

    def test_highest_card(self):
        self.assertEqual(self.card1, self.card_game.highest_card(self.card1, self.card2))

    def test_cards_total(self):
        self.assertEqual("You have a total of 13", self.card_game.cards_total(self.cards))




        