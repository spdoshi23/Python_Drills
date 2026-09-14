N = int(input("Enter a number N: "))

count = 0
previous_digit = N%10
N = N//10

while N>0:
    current_digit = N%10
    if previous_digit != current_digit:
        count = count + 1
    previous_digit = current_digit
    N = N//10

print(count)














