student = {
    "name": "Alex",
    "marks": 85
}

marks = int(input("Enter marks out of 100: "))
if marks < 0 or marks > 100:
    raise ValueError ("Marks must be between 0 and 100")
elif marks < 35:
    print("Student failed")
else:
    print("Student passed")



