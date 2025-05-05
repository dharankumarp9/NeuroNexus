def calculator():
    print("Simple Calculator")
    print("Operations: + (Add), - (Subtract), * (Multiply), / (Divide)")

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Choose an operation (+, -, *, /): ")

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                return
            result = num1 / num2
        else:
            print("Invalid operation. Please choose +, -, *, or /.")
            return

        print(f"The result is: {result}")

    except ValueError:
        print("Invalid input. Please enter numeric values.")

calculator()
