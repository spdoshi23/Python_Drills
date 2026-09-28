numbers = [3, 7, 2, 9, 4, 7, 6, 2]

lst = []
for i in numbers:
    if numbers.count(i) == 1:
        lst.append(i)

print(lst)