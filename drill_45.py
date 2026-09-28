numbers = [12, 5, 8, 21, 4, 15, 10]

lst = []
for i in numbers:
    if i%2==0:
        lst.append(numbers.index(i))
print(lst)

#  ALTERNATE WAY
numbers = [12, 5, 8, 21, 4, 15, 10]

lst = []

for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        lst.append(i)

print(lst)




