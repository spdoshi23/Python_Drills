students = {
    "Aarav": {"Python": 85, "Maths": 72, "Physics": 90},
    "Diya": {"Python": 92, "Maths": 88, "Physics": 95},
    "Kabir": {"Python": 45, "Maths": 67, "Physics": 52},
    "Meera": {"Python": 78, "Maths": 35, "Physics": 81},
    "Rohan": {"Python": 60, "Maths": 55, "Physics": 48}
}

total_marks = {}
failed_student = set()

for name, details in students.items():
    total = 0
    for subjects in details:
        total = total + details[subjects]
    
        if details[subjects] < 40:
            failed_student.add(name)
            break

    total_marks[name] = total

highest_score = 0
for name, score in total_marks.items():
    if score > highest_score:
        highest_score = score
        highest_scorer = name

print(total_marks)
print("Highest scorer =", highest_scorer)
print("Highest score =", highest_score)
print(failed_student)
























