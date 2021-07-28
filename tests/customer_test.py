import unittest
from src.pub import *
from src.customer import *
from src.drinks import *

class TestCustomer (unittest.TestCase):
    def setUp(self):
       self.customer = Customer("Phil Mitchell", 2000) 

    def test_customer_has_name(self):
        self.assertEqual("Phil Mitchell", self.customer.name)

    def test_customer_has_wallet(self):
        self.assertEqual(2000, self.customer.wallet)

