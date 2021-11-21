from art import logo

def add(n1, n2):
    return n1 + n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def subtract(n1, n2):
    return n1 - n2


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}


def calculator():
    print(logo)

    num1 = float(input("What is your first number?: "))

    for key in operations:
        print(key)

    should_continue = True
    while should_continue:
        operation_symbol = input("Enter operation: ")
        num2 = float(input("What is your next number?: "))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        yes_no = input(f"type 'y' to keep calculating with {answer}, and type 'n' to exit or type 'a' to start afresh")
        if yes_no == 'y':
            num1 = answer
        elif yes_no == 'a':
            should_continue = False
            calculator()
        else:
            break


    print("GOODBYE")