N = int(input("Enter a number N: "))

has_consecutive = False

previous_digit = N%10
N = N//10

while N>0:
    current_digit = N%10
    if previous_digit == current_digit:
        has_consecutive = True
    previous_digit = current_digit
    N = N//10

if has_consecutive:
    print("N has two consecutive equal digits")
else:
    print("N does not have two consecutive equal digits")
