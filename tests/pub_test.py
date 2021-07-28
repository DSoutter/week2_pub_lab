#import pdb
import unittest
from src.pub import *
from src.customer import *
from src.drinks import *
from src.food import *

class TestPub (unittest.TestCase):
    def setUp(self):
        self.drinks1 = Drink("Beer", 500, 2)
        self.drinks2 = Drink("Wine", 300, 2.5)
        self.drinks3 = Drink("Gin", 350, 3.5)
        self.drinks4 = Drink("White Russian", 400, 4.5)
        drinks = [self.drinks1, self.drinks2, self.drinks3, self.drinks4]
        self.pub = Pub("The Queen Vic", 10000, drinks)
        self.customer = Customer("Phil Mitchell", 2000, 45)

    def test_pub_has_name(self):
        self.assertEqual("The Queen Vic", self.pub.name)

    def test_pub_has_till(self):
        self.assertEqual(10000, self.pub.till)

    def test_remove_drinks(self):
        self.pub.remove_drinks(self.drinks1)
        self.assertEqual(3, len(self.pub.drinks))

    def test_refuse_service(self):
        self.customer.drunkenness = 7
        self.pub.refuse_service(self.customer)
        self.assertEqual("No more for you!", self.pub.refuse_service(self.customer))

    def test_sell_drink_to_customer(self):
        drink = self.pub.drinks[0]
        self.customer.buy_drink(drink)
        self.pub.increase_till(drink)
        self.assertEqual(1500, self.customer.wallet)
        self.assertEqual(10500, self.pub.till)

