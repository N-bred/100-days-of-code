class Coffee_Machine(object):
    def __init__(self):
        self.water = 300
        self.milk = 200
        self.coffee = 100
        self.money = 0

    def get_report(self):
        return f"Water: {self.water}\nMilk: {self.milk}\nCoffee {self.coffee}\nMoney: ${self.money}"
