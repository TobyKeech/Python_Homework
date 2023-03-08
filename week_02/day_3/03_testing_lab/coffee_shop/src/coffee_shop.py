class CoffeeShop:
    
    def __init__(self,name,till):
        self.name = name
        self.till = till
        self.drinks = ["tea", "coffee", "latte"]

    def drinks_list(self):
        return len(self.drinks)
