# Simple Calculator:
print("Welcome to calculator:")
print("Addition  => 1")
print("Subtraction => 2")
print("Multiplication => 3")
print("Division => 4")
print("Power => 5")
print("Exit => 6")
print("<=========================>")

available_data = [1, 2, 3, 4, 5, 6]

while True:
    try:
        operation = int(input("Enter the operation: "))
    except ValueError:
        print("Enter numbers only, not alphabets or symbols!")
        continue

    if operation in available_data:
        if operation == 6:
            print("Thank you")
            break
        else:
            # Loop for first number
            while True:
                try:
                    num1 = int(input("Enter the first number: "))
                    break
                except ValueError:
                    print("Please enter a valid number!")

            # Loop for second number
            while True:
                try:
                    num2 = int(input("Enter the second number: "))
                    break
                except ValueError:
                    print("Please enter a valid number!")

            # Perform operation
            if operation == 1:
                print("Sum of two numbers:", num1 + num2)
            elif operation == 2:
                print("Subtraction of two numbers:", num1 - num2)
            elif operation == 3:
                print("Multiplication of two numbers:", num1 * num2)
            elif operation == 4:
                if num2 == 0:
                    print("Cannot divide by zero!")
                else:
                    print("Division of two numbers:", num1 / num2)
            elif operation == 5:
                print("Power of two numbers:", num1 ** num2)
    else:
        print("Enter a valid operation (1 to 6)")
