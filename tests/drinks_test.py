import unittest
from src.pub import *
from src.customer import *
from src.drinks import *

class TestDrinks (unittest.TestCase):
    def setUp(self):
        self.drinks1 = Drink("Beer", 200)
        self.drinks2 = Drink("Wine", 300)
        self.drinks3 = Drink("Gin", 350)
        drinks = [self.drinks1, self.drinks2, self.drinks3] 

    def test_pub_has_drinks(self):
        self.assertEqual("Beer", self.drinks1.name)

    def test_drinks_has_name(self):
        self.assertEqual("Gin", self.drinks3.name)

    def test_drinks_has_price(self):
        self.assertEqual(300, self.drinks2.price)
