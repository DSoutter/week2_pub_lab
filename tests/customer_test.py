import unittest
from src.pub import *
from src.customer import *
from src.drinks import *
from src.food import *

class TestCustomer (unittest.TestCase):
    def setUp(self):
       self.customer = Customer("Phil Mitchell", 2000, 45) 
       self.customer2 = Customer("Baby", 0, 1)
       self.drinks1 = Drink("Beer", 500, 2)
       self.drinks2 = Drink("Wine", 300, 2.5)
       self.drinks3 = Drink("Gin", 350, 3.5)
       self.drinks4 = Drink("White Russian", 400, 4.5)
       drinks = [self.drinks1, self.drinks2, self.drinks3, self.drinks4]
       self.pub = Pub("The Queen Vic", 10000, drinks)

    def test_customer_has_name(self):
        self.assertEqual("Phil Mitchell", self.customer.name)

    def test_customer_has_wallet(self):
        self.assertEqual(2000, self.customer.wallet)

    def test_legal_sale(self):
        self.assertEqual(True, self.customer.legal_sale())

    def test_legal_sale_two(self):
        self.assertEqual(False, self.customer2.legal_sale())

    def test_customer_drunkenness(self):
        self.pub.sell_drink_to_customer(self.drinks1, self.customer)
        self.assertEqual(2, self.customer.drunkenness)