class Coffee_Machine_Handler:
    def __init__(self, coffee_machine):
        self.coffee_machine = coffee_machine

    def check_resources(self, coffee):
        issues = []
        if self.coffee_machine.water < coffee.water:
            issues.append("Not Enough Water")
        if self.coffee_machine.milk < coffee.milk:
            issues.append("Not Enough Milk")
        if self.coffee_machine.coffee < coffee.coffee:
            issues.append("Not Enough Coffee")

        if len(issues) == 0:
            return True

        return issues

    def handle_money(self, money, coffee):
        issues = []
        if money < coffee.cost:
            issues.append(
                f"Not enough money, received only ${money} and the cost is: ${coffee.cost}"
            )
        if len(issues) == 0:
            return True
        return issues

    def give_coffee(self, coffee):
        return f"Please enjoy your {coffee}. See you soon!"

    def make_transaction(self, money, coffee):
        self.coffee_machine.water -= coffee.water
        self.coffee_machine.milk -= coffee.milk
        self.coffee_machine.coffee -= coffee.coffee
        self.coffee_machine.money += coffee.cost

    def handle_transaction(self, money, coffee):
        resources_result = self.check_resources(coffee)

        if type(resources_result) is list:
            return resources_result

        handle_money_result = self.handle_money(money, coffee)

        if type(handle_money_result) is list:
            return handle_money_result

        self.make_transaction(money, coffee)

        return self.give_coffee(coffee)

    def get_report(self):
        return f"Water: {self.coffee_machine.water}\nMilk: {self.coffee_machine.milk}\nCoffee {self.coffee_machine.coffee}\nMoney: ${self.coffee_machine.money}"