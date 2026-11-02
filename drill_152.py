age = int(input("Enter age: "))

if age < 18 or age > 60:
    raise ValueError ("Age must be between 18 and 60")
else:
    print("Age accepted")

