correct_pin = 2468
attempts = 0

pin = int(input("Enter PIN: "))
while attempts < 3:
    if pin != correct_pin:
        print("Incorrect PIN")
    else:
        print("Login successful!")
        break
    attempts += 1
    if attempts < 3:
        pin = int(input("Enter PIN: "))
else:
    print("Account locked!")

