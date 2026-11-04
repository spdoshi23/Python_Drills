marks = int(input("Enter marks: "))

result = "Invalid marks" if marks<0 or marks>100 else "Excellent" if marks>=90 else "Distinction" if 75<=marks<=89 else "Pass" if 40<=marks<=74 else "Fail"
print(result)