N = int(input("Enter a number N: "))

is_divisible_by_3 = False

while N>0:                                    
    current_digit = N%10
    if current_digit%3 == 0:
        is_divisible_by_3 = True
     
    N = N//10
    
if is_divisible_by_3:
    print("N has a digit divisible by 3")
else:
    print("N doesn't have digits divisible by 3")
    
















