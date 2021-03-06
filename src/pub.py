class Pub:
    def __init__(self, name, till, drinks):
        self.name = name
        self.till = till
        self.drinks = drinks
    
    def remove_drinks(self, drink):
        self.drinks.remove(drink)
        #remove drinks method

    def increase_till(self, drink):
        self.till += drink.price

    def refuse_service(self, customer):
        if customer.drunkenness >=6:
            return "No more for you!"
        
# check what the customer wants to buy
# method to check if customer has enough money to buy drink
# if so, reduce wallet by drink price
# increase till by drink price

    def sell_drink_to_customer(self, drink, customer):
        self.refuse_service(customer)
        customer.buy_drink(drink)
        self.increase_till(drink)
        self.remove_drinks(drink)
        customer.customer_drunkenness(drink)