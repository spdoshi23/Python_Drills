N = int(input("Enter a number N: "))

for k in range(N, 0, -1):
    if k%4==0:
        print(k)
        break

#               ALTERNATE WAY
N = int(input("Enter a number N: "))

for k in range(4, N+1, 4):
    if k+4>N:
        break
print(k)


