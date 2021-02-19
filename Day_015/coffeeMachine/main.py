from CoffeeMachine import Coffee_Machine
from Expresso import Expresso
from Latte import Latte
from Capuccino import Capuccino


def main():
    if __name__ == "__main__":
        print("Welcome to the Coffee Machine")

        # Instances

        coffee_machine = Coffee_Machine()
        expresso = Expresso()
        latte = Latte()
        capuccino = Capuccino()

        print(coffee_machine.get_report())


main()