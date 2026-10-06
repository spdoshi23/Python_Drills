def process_numbers(numbers):
    even_sum = 0
    odd_sum = 0
    i = 0 
    while i < len(numbers):
        if numbers[i] > 0:
            if numbers[i]%2 == 0:
                even_sum = even_sum + numbers[i]
            else:
                odd_sum = odd_sum + numbers[i]
        i = i + 1
    return (odd_sum, even_sum)

print(process_numbers([4, -3, 7, 2, -8, 5]))





















