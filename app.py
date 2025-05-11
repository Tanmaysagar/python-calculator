# Simple Calculator Program in Python

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero is not allowed."
    return x / y

def calculator():
    print("Simple Calculator")
    print("-----------------")
    
    # User inputs
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return
    
    print("\nChoose the operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    operation = input("Enter your choice (1/2/3/4): ")

    # Perform the calculation based on user choice
    if operation == '1':
        print(f"\nResult: {num1} + {num2} = {add(num1, num2)}")
    elif operation == '2':
        print(f"\nResult: {num1} - {num2} = {subtract(num1, num2)}")
    elif operation == '3':
        print(f"\nResult: {num1} * {num2} = {multiply(num1, num2)}")
    elif operation == '4':
        print(f"\nResult: {num1} / {num2} = {divide(num1, num2)}")
    else:
        print("Invalid operation choice! Please select a valid option.")
calculator()
