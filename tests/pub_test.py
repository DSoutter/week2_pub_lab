#import pdb
import unittest
from src.pub import *
from src.customer import *
from src.drinks import *

class TestPub (unittest.TestCase):
    def setUp(self):
        self.drinks = Drink("Vodka", 500)
        self.pub = Pub("The Queen Vic", 10000, self.drinks)
        self.customer = Customer("Phil Mitchell", 2000)

    def test_pub_has_name(self):
        self.assertEqual("The Queen Vic", self.pub.name)

    def test_pub_has_till(self):
        self.assertEqual(10000, self.pub.till)

    def test_sell_drink_to_customer(self):
        drink = self.drinks
        customer = self.customer
        self.pub.increase_till(drink)
        self.customer.buy_drink(drink)
        self.assertEqual(1500, self.customer.wallet)