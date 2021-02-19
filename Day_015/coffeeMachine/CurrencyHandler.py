class Currency_Handler:
    @staticmethod
    def calculate_money(all_money):
        quarters, dimes, nickles, pennies = all_money
        return (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)

    @staticmethod
    def calculate_change(money, cost):
        return round(money - cost, 2)