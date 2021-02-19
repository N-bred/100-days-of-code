from Coffee import Coffee


class Expresso(Coffee):
    def __init__(self, water=50, milk=0, coffee=18, cost=1.5):
        super().__init__(water, milk, coffee, cost)
