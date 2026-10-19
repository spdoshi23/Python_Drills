def count_digit(n, d):
    if n == 0 and d==0:
        return 1
    if n == 0:
        return 0
    last_digit = n % 10
    remaining = n // 10
    if last_digit == d:
        return 1 + count_digit(remaining, d)
    elif last_digit != d:
        return count_digit(remaining, d)


print(count_digit(12232, 2))
print(count_digit(5555, 5))
print(count_digit(1234, 7))
print(count_digit(8, 8))
print(count_digit(0, 0))
