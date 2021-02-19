from Coffee import Coffee


class Capuccino(Coffee):
    def __init__(self, water=250, milk=100, coffee=24, cost=3.0):
        super().__init__(water, milk, coffee, cost)
