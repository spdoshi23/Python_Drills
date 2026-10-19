def count_divisible(n, d):
    last_digit = n % 10
    remaining = n // 10
    if n < 10:
        if n % d == 0:
            return 1
        else:
            return 0

    elif last_digit % d == 0:
        return 1 + count_divisible(remaining, d)
    else:
        return count_divisible(remaining, d)

print(count_divisible(123456, 2))  # 3  
print(count_divisible(2468, 4))    # 2  
print(count_divisible(13579, 2))   # 0
print(count_divisible(888, 4))     # 3
print(count_divisible(7, 7))       # 1