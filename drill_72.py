numbers = [4, 7, 4, 2, 9, 7, 4, 5, 2, 8, 7]

def analyze_numbers(numbers):
    lst = []
    for i in numbers:
        if numbers.count(i)>1 and i not in lst:
            lst.append(i)
    return lst

result = analyze_numbers(numbers)
print(result)








