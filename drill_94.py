def count_odd_digits(n):
    last_digit = n % 10
    remaining = n // 10
    if n < 10:
        if n%2 != 0:
            return 1
        else:
            return 0
    elif last_digit%2 != 0:
        return 1 + count_odd_digits(remaining)
    elif last_digit%2 == 0:
        return count_odd_digits(remaining)

print(count_odd_digits(12345))
print(count_odd_digits(2468))
print(count_odd_digits(1357))
print(count_odd_digits(1234))
print(count_odd_digits(0))