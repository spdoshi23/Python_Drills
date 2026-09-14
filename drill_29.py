N = int(input("Enter a number N: "))

changes = 0
previous_even = ((N%10)%2==0)

while N>0:
    current_even = ((N%10)%2==0)
    if current_even != previous_even:
        changes = changes+1

    previous_even = current_even
    N= N//10
    
print(changes)