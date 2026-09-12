N = int(input("Enter a number N: "))

count = 0

while N>0:
    count = count + 1
    N = N//10
print(count)