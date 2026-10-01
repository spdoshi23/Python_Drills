N = int(input("Enter a number N: "))

sum = 0

while N>0:
    digit = N%10
    sum = sum + digit
    N = N//10

print(sum)











