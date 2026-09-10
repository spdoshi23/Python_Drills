N = int(input("Enter a number N: "))
count = 0
sum = 0

for k in range(1, N+1):
    if k%3==0:
        count = count + 1
        sum = sum + k 

print(sum)
print(count)