numbers = [4, 7, 4, 2, 7, 4, 9, 2, 7, 5]

n = int(input("Enter number:"))

if n in numbers:
    if numbers.count(n)>=2:
        print('frequent')
    else:
        print('not frequent')
else:
    print('n not in list')

# alternate way
count = 0

for i in numbers:
    if i == n:
        count += 1

print(n, "occourred", count, "times")
if count>= 2:
    print("frequent")
else:
    print('not frequent')
    


