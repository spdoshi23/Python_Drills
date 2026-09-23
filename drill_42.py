N = int(input("Enter a number N: "))

sign = 1
answer = 0

while N>0:
    digit = N%10
    answer = answer + (digit)*sign
    sign = sign * -1
    N = N//10

print(answer)



















