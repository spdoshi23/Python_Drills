N = int(input("Enter a number N: "))

current_run = 1
longest_run = 1

previous_digit = N%10
N = N//10

while N>0:
    currernt_digit = N%10
    if currernt_digit < previous_digit:
        current_run = current_run + 1
    else:
        current_run = 1                              #because if sequence breaks if current digit is larger than previous digit then we have to start with 1 bcz current_digit is already exmining one digit 
    if current_run > longest_run:
        longest_run = current_run

    previous_digit = currernt_digit
    N = N//10

print(longest_run)




















