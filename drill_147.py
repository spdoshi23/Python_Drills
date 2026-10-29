try:
    units = input("Enter units consumed:")
    units = int(units)
    valid = True
    if units < 0:
        valid = False
        print("Units consumed must be a positive integer")
except ValueError:
    print("Enter valid integer")
else:
    if valid:
        if 0 <= units <= 100:
            cost = units * 2
        elif 101<= units <= 200:
            cost = (100 * 2) + ((units - 100) * 3)
        else:
            cost = (100 * 2) + (100 * 3) + ((units - 200) * 5)
        print("Electricity bill =", cost)
finally:
    print("Electricity bill calculation attempt completed.")




