students = {
    "Aarav": [78, 85, 92],
    "Priya": [90, 88, 95],
    "Rahul": [45, 55, 40],
    "Sneha": [67, 72, 80],
    "Karan": [30, 35, 25]
}

result = {}
passed_students = []
needs_improvement = set()

for name, marks in students.items():
    total = sum(marks)
    average = total/len(marks)
    if all(mark >= 40 for mark in marks):
        status = "pass"
    else:
        status = "fail"
    result[name] = {
    "total": total,
    "average": round(average, 2),
    "status": status
}
    if status == "pass":
        passed_students.append(name)
    if average < 50:
        needs_improvement.add(name)

highest_average = 0
topper = None
for name, details in result.items():
    if details["average"] > highest_average:
        topper = name
        highest_average = details["average"]
    

print(result)
print(passed_students)
print(needs_improvement)
print(topper)











