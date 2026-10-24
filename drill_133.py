students = {
    "Aarav": {"marks": 85, "attendance": 90},
    "Priya": {"marks": 32, "attendance": 95},
    "Rohan": {"marks": 67, "attendance": 60},
    "Sneha": {"marks": 28, "attendance": 45},
    "Kabir": {"marks": 92, "attendance": 80},
    "Ishita": {"marks": 74, "attendance": 35}
}

results = {}
high_performers = {}
low_attendance = []

total = 0
for name, details in students.items():
    if details["marks"] >= 35 and details["attendance"] >= 75:
        results[name] = "elegible"
    else:
        results[name] = "not elegible"

    total = details["marks"] + total

    if details["marks"] >= 75:
        high_performers[name] = details

    if details["attendance"] < 50:
        low_attendance.append(name)

average = total/len(students)

for i in low_attendance:
    students.pop(i)

print(students)
print(results)
print(high_performers)
print(average)






















