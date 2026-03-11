print("........................CALCULATOR........................")
print("..........................................................")

while True:

    print("..........................................................")
    print("Enter a number to perform the operation:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Remainder\n6. Power\n7. Square\n8. Square Root\n9. Cube\n10. Cube Root\n11. Quotient\n12. Even/Odd check\n13. Exit")
    
    choice = int(input("Enter your choice (1-13): "))
    if choice < 1 or choice > 13 :
        print("Invalid choice. Please enter a number between 1 and 13.")
        continue
    
    if choice == 1:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 + num2
        print(f"The sum of {num1} and {num2} is: {result}")
    elif choice == 2:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 - num2
        print(f"The difference of {num1} and {num2} is: {result}")
    elif choice == 3:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 * num2
        print(f"The product of {num1} and {num2} is: {result}")
    elif choice == 4:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 / num2
        print(f"The quotient of {num1} and {num2} is: {result}")
    elif choice == 5:
        num1  = float(input("Enter the first number: "))
        num2  = float(input("Enter the second number: "))
        result = num1 % num2
        print(f"The remainder of {num1} divided by {num2} is: {result}")
    elif choice ==6 :
        num1  = float(input("Enter the first number: "))
        num2  = float(input("Enter the second number: "))
        result = num1 ** num2
        print(f"{num1} raised to the power of {num2} is: {result}")
    elif choice == 7:
        num1 = float(input("Enter the number: "))
        result = num1 ** 2
        print(f"The square of {num1} is: {result}")
    elif choice == 8:
        num1 = float(input("Enter the number: "))
        result = num1 ** (1/2)
        print(f"The square root of {num1} is: {result}")
    elif choice == 9:
        num1 = float(input("Enter the number: "))
        result = num1 ** 3
        print(f"The cube of {num1} is: {result}")
    elif choice == 10:
        num1 = float(input("Enter the number: "))
        result = num1 ** (1/3)
        print(f"The cube root of {num1} is: {result}")
    elif choice == 11:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 // num2
        print(f"The quotient of {num1} divided by {num2} is: {result}")
    elif choice == 12:
        num1 = int(input("Enter the number: "))
        if num1 % 2 == 0:
            print(f"{num1} is an even number.")
        else:
            print(f"{num1} is an odd number.")
    elif choice == 13:
        print("Exiting the calculator. Goodbye!")
        break
    