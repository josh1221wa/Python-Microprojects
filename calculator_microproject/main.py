import art


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {"+": add, "-": subtract, "*": multiply, "/": divide}


def calculator():
    print(art.logo)

    should_continue = True

    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)

    while should_continue:
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(
            f'type "y" to continue calculating with {answer}, or type "n" to start a new calculation: ')

        if choice == 'y':
            num1 = answer
            should_continue = True
        else:
            calculator()
            should_continue = False


calculator()
