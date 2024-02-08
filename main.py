# A simple calculator
from replit import clear


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

while True:  # continuous calculation prompt

    first_number = int(input("Please provide first number: "))
    second_number = int(input("Please provide second number: "))

    operator = []
    for symbol in operations:
        operator += symbol

    operation_symbol = input(f"Pick an operation {operator} : ")

    calculation_function = operations[operation_symbol]
    answer = calculation_function(first_number, second_number)

    print(f"{first_number} {operation_symbol} {second_number} = {answer}")

    if input("Would like to exit? Type y/n :") == "y":
        break
    else:
        clear()  # clears the terminal
