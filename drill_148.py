try:    
    name = input("Enter your name: ")
    sub1 = input("Enter marks: ")
    sub2 = input("Enter marks: ")
    sub3 = input("Enter marks: ")
    sub1 = int(sub1)
    sub2 = int(sub2)
    sub3 = int(sub3)
    valid = True
    if sub1 < 0 or sub1 > 100:
        valid = False
        print("Marks must be between 0 to 100")
    if sub2 < 0 or sub2 > 100:
        valid = False
        print("Marks must be between 0 to 100")
    if sub3 < 0 or sub3 > 100:
        valid = False
        print("Marks must be between 0 to 100")
except ValueError:
    print("Enter valid integer")
else:
    if valid:
        marks = {}
        marks.update({"sub1" : sub1, "sub2" : sub2, "sub3" : sub3})
        total =sum(marks.values())
        percent = (total / (len(marks) * 100)) * 100
        print(total)
        print(percent)
        if sub1 >= 40 and sub2 >= 40 and sub3 >= 40:
            print("pass")
        else:
            print("fail")
finally:
    print("Student result calculation attempt completed.")

