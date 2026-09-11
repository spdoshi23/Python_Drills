N = int(input("Enter a number N: "))
reverse = 0

while N>0:
    digit = N%10
    reverse = (reverse*10) + digit
    N = N//10
    
print(reverse)

if reverse%3==0:
    print("Reversed digit is divisible by 3")
else:
    print("Reversed digit is not divisible by 3")
    