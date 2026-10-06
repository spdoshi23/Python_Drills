def analyze_numbers(numbers):
    count = 0
    total = 0
    i = 0
    while i < len(numbers):
        if numbers[i] < 0:
            i = i + 1
            continue
        elif numbers[i] % 2==0:
            count += 1
            total = total + numbers[i]
        i = i + 1
    return(count, total)

print(analyze_numbers([4, -2, 7, 8, -5, 6, 3]))








