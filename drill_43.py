numbers = [12, 5, 8, 21, 4, 15, 10]

lst = [i for i in numbers if i>10]
print(lst)


#             ALTERNATE WAY
numbers = [12, 5, 8, 21, 4, 15, 10]
lst=[]
for i in numbers:
    if i>10:
        lst.append(i)