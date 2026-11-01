students = [
    {"name": "Aman", "marks": [78, 85, 92]},
    {"name": "Riya", "marks": [35, 42, 38]},
    {"name": "Kabir", "marks": [60, 55, 70]},
    {"name": "Neha", "marks": [90, 95, 88]},
    {"name": "Dev", "marks": [40, 40, 40]}
]

passed = []
failed = []
unique_marks = set()
highest_total = 0
for i in students:
    total = sum(i["marks"])
    if total > highest_total:
        highest_total = total
        topper_name = i["name"]
    average = total / len(i["marks"])
    if all(mark >= 40 for mark in i["marks"]):
        print(f"name - {i["name"]}, Total - {total}, Average - {average}, Result - Pass")
        passed.append(i["name"])
    else:
        print(f"name - {i["name"]}, Total - {total}, Average - {average}, Result - Fail")
        failed.append(i["name"])
    for mark in i["marks"]:
        unique_marks.add(mark)

print(f"Passed Students - {passed}")
print(f"Failed Students - {failed}")
print(f"Number passed - {len(passed)}")
print(f"Number failed - {len(failed)}")
print(f"Topper - {topper_name}, with {highest_total} marks")
print(f"Unique marks - {unique_marks}")












