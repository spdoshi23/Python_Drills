try:
    max_marks = 500
    marks = input("Enter marks: ")
    marks = int(marks)
    valid = True
    if marks < 0 or marks > max_marks:
        valid = False
        print("Marks must be between 0 and 500.")
    else:
        percentage = marks / max_marks * 100
except ValueError:
    print("Invalid input! Please enter integers.")
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    if valid:
        print(percentage)
finally:
    print("Calculation attempt completed.")













