class Pub:
    def __init__(self, name, till, drinks):
        self.name = name
        self.till = till
        self.drinks = drinks
    
    def increase_till(self, drink):
        self.till += drink.price

# check what the customer wants to buy
# method to check if customer has enough money to buy drink
# if so, reduce wallet by drink price
# increase till by drink price

    def sell_drink_to_customer(self, drink, customer):
        self.increase_till(drink)
        customer.buy_drink(drink)