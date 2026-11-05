students = ["Aarav", "Priya", "Rahul", "Sneha", "Karan"]
marks = [85, 92, 67, 92, 78]

highest_mark = None
for mark in marks:
    if highest_mark is None or mark > highest_mark:
        highest_mark = mark

print(f"Highest marks: {highest_mark}\n")

for i, mark in enumerate(marks, start=1):
    if mark == highest_mark:
        print(f"Roll No. {i}: {students[i - 1]}")
















