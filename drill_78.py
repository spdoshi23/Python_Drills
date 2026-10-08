def find_largest(numbers):
    largest = 0
    i = 0
    while i < len(numbers):
            if numbers[i] > largest:
                largest = numbers[i]
            i = i + 1
    if largest == 0:
         return None
    else:
        return largest

print(find_largest([-4, 7, 2, -9, 15, 6]))


name = "shushant"
print(f"my name is {name}")



    

















