def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

def calculator():
    print("Simple Calculator")
    print("Operations: +, -, *, /")
    print("Enter 'q' to quit")

    while True:
        operation = input("Enter operation (+, -, *, /) or 'q' to quit: ")

        if operation == 'q':
            print("Exiting the calculator. Goodbye!")
            break

        if operation in ('+', '-', '*', '/'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if operation == '+':
                    print(f"{num1} + {num2} = {add(num1, num2)}")
                elif operation == '-':
                    print(f"{num1} - {num2} = {subtract(num1, num2)}")
                elif operation == '*':
                    print(f"{num1} * {num2} = {multiply(num1, num2)}")
                elif operation == '/':
                    print(f"{num1} / {num2} = {divide(num1, num2)}")

            except ValueError:
                print("Invalid input! Please enter a valid number.")

        else:
            print("Invalid operation! Please enter a valid operation.")

calculator()
