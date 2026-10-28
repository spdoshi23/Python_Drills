try:
    a = input("Enter first number: ")
    b = input("Enter second number: ")
    a = int(a)
    b = int(b)
    result = a / b
except ValueError:
    print("Invalid input! Please enter integers.")
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print(result)
finally:
    print("Program execution completed.")
