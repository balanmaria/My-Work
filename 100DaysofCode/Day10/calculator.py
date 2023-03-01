import art

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
    "/": divide
}

def calculator():
    print(art.logo)
    num1=float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    should_continue=True

    while should_continue:
        operation=input("Pick an operation: ")
        num2=float(input("What's the next number?: "))
        answer=operations[operation](num1, num2)
        print(f"{num1} {operation} {num2} = {answer}")

        result=input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
        if result == "y":
            num1=answer
        else:
            should_continue=False
            calculator()

calculator()