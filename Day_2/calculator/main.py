def calc_operation(first, second, op):
    if op == "+":
        result = first + second
    elif op == "-":
        result = first - second
    elif op == "*":
        result = first * second
    elif op == "/":
        result = first / second
    else:
        raise Exception(f"Bad operator {op}")

    return result


def get_inputs(is_next=False, default_value=0):
    if is_next:
        first_input = default_value
    else:
        first_input = int(input("Enter the first number: "))


    operation = input("Enter the type of operation: + - / *: ")
    second_input = int(input("Enter the second number: "))
    return first_input, operation, second_input


def main():
    if __name__ == "__main__":
        print("Welcome to the Calculator")

        is_calculating = True
        is_next = False
        result = 0

        while is_calculating:
            first_input, operation, second_input = get_inputs(is_next, result)
            result = calc_operation(first_input, second_input, operation)

            print(f"Result: {result}")
            again = input("Do you want to continue calculating with the result? y or n: ")

            if again.lower() == "n":
                is_calculating = False
            elif again.lower() == "y":
                is_next = True
            else:
                raise Exception("Bad option")

        return print(f"The final result is {result}")


main()