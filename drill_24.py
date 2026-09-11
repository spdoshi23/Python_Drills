N = int(input("Enter a number N: "))

previous = N % 10
N = N // 10

increasing = True 


while N>0: 
    digit = N%10
    if digit>=previous:
        increasing = False 
        break
    previous = digit
    N = N//10

if increasing==False:
    print("Number is not increasing")
else:
    print("Number is increasing")


    
    
        

