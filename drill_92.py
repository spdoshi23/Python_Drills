def sum_digits(n):
    last_digit = n%10
    remaining = n//10
    if remaining < 10:
        return last_digit + remaining
    else:
        return last_digit + sum_digits(remaining)

print(sum_digits(1234))
print(sum_digits(568))
print(sum_digits(999))
print(sum_digits(7))
