try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    result = a/b
    print(result)
except ValueError:
    print("Please enter valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")









