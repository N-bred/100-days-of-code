from Coffee import Coffee


class Latte(Coffee):
    def __init__(self, water=200, milk=150, coffee=24, cost=2.5):
        super().__init__(water, milk, coffee, cost)
