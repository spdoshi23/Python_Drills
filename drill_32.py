N = int(input("Enter a number N: "))

previous_digit = N%10
N = N//10

decreasing = True

while N>0:
    current_digit = N%10
    if current_digit>=previous_digit:
        decreasing = False
    previous_digit = current_digit
    N = N//10

if decreasing:
    print("N is strictly inccreasing")
else:
    print("N is not strictly increasing")
    












