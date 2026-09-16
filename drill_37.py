N = int(input("Enter a number N: "))

previous_digit = N%10
N = N//10

repeating_count = 1

max_run = 1                                              #bcz, every number will occur atleast once

while N>0:
    current_digit = N%10
    if previous_digit == current_digit:
        repeating_count = repeating_count + 1
    else:
        repeating_count = 1
    if repeating_count > max_run:
        max_run = repeating_count
    previous_digit = current_digit
    N = N//10

print(max_run)















