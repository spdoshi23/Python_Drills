students = ["Aarav", "Priya", "Rahul", "Sneha", "Karan"]
marks = [85, 32, 67, 28, 91]

failed = 0
for index, mark in enumerate(marks, start=1):
    if mark >= 40:
        print(f"Roll No. {index}: {students[index-1]} - PASS")
    else:
        print(f"Roll No. {index}: {students[index-1]} - FAIL")
        failed += 1
print("Number of students failed =", failed)