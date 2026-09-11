N = int(input("Enter a number N: "))

largest = 0

while N>0:
    digit = N%10
    if(digit>largest):
        largest = digit
    N = N//10

print(largest)