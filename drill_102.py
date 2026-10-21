list1 = [2, 4, 6, 8, 10, 4]
list2 = [1, 4, 5, 8, 10, 10]

l1 = set(list1)
l2 = set(list2)

unique = set()

for i in l1:
    if i in l2:
        unique.add(i)

print(unique)



