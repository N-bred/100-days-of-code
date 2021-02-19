class Coffee(object):
    def __init__(self, water=0, milk=0, coffee=0, cost=0):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.cost = cost

    def __str__(self):
        return f"{self.__class__.__name__}"