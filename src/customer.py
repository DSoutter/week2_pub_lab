class Customer:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet



    def buy_drink(self, bev):
        if self.wallet >= bev.price:
            self.wallet -= bev.price