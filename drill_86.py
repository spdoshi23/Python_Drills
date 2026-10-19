def total(n):
    if n == 0:
        return 0
    else:
        return n + total(n-1)

print(total(5))
