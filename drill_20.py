N = int(input("Enter a positive number N:  "))
sum_even = 0
sum_odd = 0

for k in range(0, N+1):
    if k%2==0:
        sum_even = sum_even + k
    else:
        sum_odd = sum_odd + k

print(sum_odd)
print(sum_even)
        