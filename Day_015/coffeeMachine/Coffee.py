class Coffee(object):
    def __init__(self, water=0, milk=0, coffee=0, cost=0):
        self.ingredients = {"water": water, "milk": milk, "coffee": coffee}
        self.cost = cost