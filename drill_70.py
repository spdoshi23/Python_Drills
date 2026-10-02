numbers = [12, 5, 8, 21, 4, 15, 10]

def get_even_numbers(numbers):
    lst = []
    for i in numbers:
        if i%2==0:
            lst.append(i)
    return lst

result = get_even_numbers(numbers)
print(result)















