def calculator():
    while True:
        print("Simple calculator")
        print("Please enter two numbers and choose an operation.")
    
    
        num1 = float(input("Enter the number1: "))
        num2 = float(input("Enter the number2: "))

    
        print("\nOperations:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
    
        operation = input("Choose an operation (1/2/3/4): ")

    
        if operation == '1':
            result = num1 + num2
            operation_sign = '+'
        elif operation == '2':
            result = num1 - num2
            operation_sign = '-'
        elif operation == '3':
            result = num1 * num2
            operation_sign = '*'
        elif operation == '4':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                return
            result = num1 / num2
            operation_sign = '/'
        elif operation == '5':
            break
        else:
            print("Invalid operation choice.")
            return
    
    
        print(f"\nThe result of {num1} {operation_sign} {num2} is: {result}")


calculator()
