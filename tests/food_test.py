import unittest
from src.pub import *
from src.customer import *
from src.drinks import *
from src.food import *

class TestFood (unittest.TestCase):
    def setUp(self):
        self.food1 = Food("Burger", 1000, 4.0)
        self.food2 = Food("Fish and Chips", 1500, 5.0)
        self.food3 = Food("Chips", 500, 2.5)
        food = [self.food1, self.food2, self.food3] 

    def test_pub_has_food(self):
        self.assertEqual("Burger", self.food1.name)

    def test_pub_has_food(self):
        self.assertEqual("Fish and Chips", self.food2.name)

    def test_food_has_price(self):
        self.assertEqual(1000, self.food1.price)

    def test_food_has_rejuvenation(self):
        self.assertEqual(2.5, self.food3.rejuvenation_level)
