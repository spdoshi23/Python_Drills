numbers = [4, 7, 2, 7, 9, 4, 7, 2]
lst = []

for number in numbers:
    if numbers.count(number) > 1 and number not in lst:
        lst.append(number)
        
print(lst)











