N = int(input("Enter a number N: "))

while N>0:
    digit = N%10
    previous = digit
    N = N//10
    if digit>=previous:
        print("number is not strictly increasing")
    else:
        print("number is strictly increasing")