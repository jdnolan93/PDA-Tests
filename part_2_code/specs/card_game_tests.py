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

        