class Customer:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet

# check what the customer wants to buy
# method to check if customer has enough money to buy drink
# if so, reduce wallet by drink price
# increase till by drink price

    def buy_drink(self, bev, pub):
        if self.wallet >= bev.price:
            self.wallet -= bev.price
            pub.increase_till()