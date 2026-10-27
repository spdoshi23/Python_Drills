try:
    sub1 = input("Enter marks:")
    sub2 = input("Enter marks:")
    sub3 = input("Enter marks:")
    sub1 = int(sub1)
    sub2 = int(sub2)
    sub3 = int(sub3)
    valid = True
    if (sub1 < 0 or sub2 < 0 or sub3 < 0) or (sub1 > 100 or sub2 > 100 or sub3 > 100):
        valid = False
        print("Marks must be between 0 and 100!")
    if valid:
        total = sub1 + sub2 + sub3
        print(total)
except ValueError:
    print("Invalid marks entered!")


