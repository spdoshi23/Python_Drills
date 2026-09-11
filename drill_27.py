N = int(input("Enter a number N: "))

prev_digit = N%10
N = N//10

found = False

while N>0:
    digit = N%10
    if(digit == prev_digit):
        found = True
        break
    else:
        N = N//10
        prev_digit = digit
    
if found:
    print("YES")
else:
      print("NO")