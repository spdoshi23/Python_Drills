numbers = (4, 7, 4, 2, 9, 4, 7, 5)

N = int(input("Enter a number N: "))

if N in numbers:
    print(numbers.count(N))
    print(numbers.index(N))
else:
    print('not found')














