students = {
    "Aarav": 85,
    "Priya": 34,
    "Rohan": 67,
    "Sneha": 28,
    "Kabir": 45,
    "Ishita": 91
}

results = {}

for student, mark in students.items():
    if mark >= 35:
        results.update({student: "pass"})
    else:
        results.update({student: "fail"})

print(results)



























