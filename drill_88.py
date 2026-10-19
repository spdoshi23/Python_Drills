def power(a, b):
    if (a == 1 or b == 0):
        return 1
    else:
        return (a *  power(a, b-1))

print(power(2, 4))
print(power(1, 500))
print(power(6, 0))
print(power(5, 4))
print(power(3, 2))