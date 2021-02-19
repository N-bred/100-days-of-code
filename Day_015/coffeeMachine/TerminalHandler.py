class Terminal_Handler:
    @staticmethod
    def get_money_from_input():
        quarters = float(input("How many quarters?: $"))
        dimes = float(input("How many dimes?: $"))
        nickles = float(input("How many nickles?: $"))
        pennies = float(input("How many pennies?: $"))

        return quarters, dimes, nickles, pennies

    @staticmethod
    def log_errors_by_list(list_of_errors):
        for error in list_of_errors:
            print(error)

    @staticmethod
    def handle_input(text):
        return input(text)