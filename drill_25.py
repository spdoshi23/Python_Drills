N = int(input("Enter a number N: "))
D = int(input("Enter a number D: "))

count = 0


while N>0:  
    digit = N%10
    if(digit == D):
        count = count + 1
    
    N = N//10
    

print(count)