numbers = [12, 5, 8, 21, 4, 15, 10, 7, 18, 3]

def process_numbers(numbers):
    lst = []
    for i in numbers:
        if i%2 == 0:
            lst.append(i**2)
        else:
            continue
    return lst

result = process_numbers(numbers)
print(result)
















