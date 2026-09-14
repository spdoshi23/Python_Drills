N = int(input("Enter a number N: "))

has_adjacent_equal = False

previous_digit = N%10
N = N//10

while N>0:
    current_digit = N%10
    if previous_digit == current_digit:
        has_adjacent_equal = True
    previous_digit = current_digit
    N = N//10

if has_adjacent_equal:
    print("Has equal adjacent diigits")
else:
    print("Doesn't have equal adjacent digits")









