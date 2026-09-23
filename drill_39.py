N = int(input("Enter a number N: "))

largest = -1
sec_largest = -1

while N>0:
    current_digit = N%10
    if current_digit > largest:
        sec_largest = largest
        largest = current_digit
        
    if current_digit < largest:
        if current_digit > sec_largest:
            sec_largest = current_digit
        if current_digit < sec_largest:
            pass

    N = N//10
    
if sec_largest == -1:
    print("Second largest digit does not exist")
else:
    print(sec_largest)






















