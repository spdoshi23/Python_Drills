N = int(input("Enter a number N: "))

count = 0

def compare(right_number, middle_number, left_number):
    if (middle_number>right_number) and (middle_number>left_number):
        return True
    else:
        return False
while N>=100:
    right_number = N%10
    middle_number = (N%100)//10
    left_number = (N%1000)//100

    result = compare(right_number, middle_number, left_number)
    if result is True:
        count += 1
    N = N//10
    
print(count)

    






