from CoffeeMachine import Coffee_Machine
from CoffeeMachineHandler import Coffee_Machine_Handler
from Expresso import Expresso
from Latte import Latte
from Capuccino import Capuccino
from TerminalHandler import Terminal_Handler
from CurrencyHandler import Currency_Handler


def handling_loop(coffee_machine_handler, expresso, latte, capuccino):
    while True:
        answer = Terminal_Handler.handle_input(
            "What would you like? (expresso/latte/capuccino): "
        )

        if answer.lower() == "off":
            break
        elif answer.lower() == "report":
            print(coffee_machine_handler.get_report())
        else:
            if answer.lower() == "expresso":
                current_coffee = expresso
            elif answer.lower() == "latte":
                current_coffee = latte
            elif answer.lower() == "capuccino":
                current_coffee = capuccino
            else:
                Terminal_Handler.log_errors_by_list(["Wrong option"])
                return handling_loop(coffee_machine_handler, expresso, latte, capuccino)

            # Handle coffee transaction
            all_money = Terminal_Handler.get_money_from_input()
            money = Currency_Handler.calculate_money(all_money)
            result_from_transaction = coffee_machine_handler.handle_transaction(
                money, current_coffee
            )

            if type(result_from_transaction) is list:
                Terminal_Handler.log_errors_by_list(result_from_transaction)
                print("You get your money refunded.")
            elif type(result_from_transaction) is str:
                change = Currency_Handler.calculate_change(money, current_coffee.cost)
                print(result_from_transaction)
                print(f"Your total change is: ${change}")


def main():
    if __name__ == "__main__":
        print("Welcome to the Coffee Machine")

        # Instances

        coffee_machine = Coffee_Machine()
        coffee_machine_handler = Coffee_Machine_Handler(coffee_machine)
        expresso = Expresso()
        latte = Latte()
        capuccino = Capuccino()

        # Input loop

        handling_loop(coffee_machine_handler, expresso, latte, capuccino)


main()