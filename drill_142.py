try:
    age = input("Enter your age:")
    age = int(age)
    if age < 0:
        print("Age cannot be negative!")
    elif age > 120:
        print("Age seems unrealistic!")
    else:
        print(f"Valid age: {age}")
except ValueError:
    print("Invalid age entered!")

