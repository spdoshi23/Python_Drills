N = int(input("Enter a number N: "))

previous_digit = N%10
N = N//10

is_alterating = True

while N>0:
    current_digit = N%10
    if current_digit%2==0 and previous_digit%2==0:
        is_alterating = False
    if current_digit%2!=0 and previous_digit%2!=0:
        is_alterating = False

    previous_digit = current_digit
    N = N//10

if is_alterating:
    print("N has alternating parity")
else:
    print("N doesn't have alternating parity")









