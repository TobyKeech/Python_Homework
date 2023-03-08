class CoffeeShop:
    
    def __init__(self,name,till,price):
        self.name = name
        self.till = till
        self.drinks = ["tea", "coffee", "latte"]
        self.price = price

    def drinks_list(self):
        return len(self.drinks)
    
    def add_cash_to_till(self,amount):
         self.till += amount
         
    def sell_drink_to_customer(self,customer, price):
        self.coffeeshop.drinks
        self.customer.wallet.reduce_cash(price)
        self.add_cash_to_till
