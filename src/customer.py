class Customer:
    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkenness = 0.0

    def legal_sale(self):
        if self.age >= 18:
            return True
        else:
            return False

    def buy_drink(self, drink):
        self.legal_sale()
        if self.wallet >= drink.price:
            self.wallet -= drink.price

# for drunkenness, customer needs to have a drink
# need to buy to have a drink
# customer needs to add alcohol level to drunkenness for each drink
# 

    def customer_drunkenness(self, drink):
        self.drunkenness += drink.alcohol_level
