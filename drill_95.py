def product_digits(n):
    last_digit = n % 10
    remaining = n // 10
    if n < 10:
        return n
    else:
        return last_digit * product_digits(remaining)

print(product_digits(1234))  # 24
print(product_digits(234))   # 24
print(product_digits(555))   # 125
print(product_digits(7))     # 7
print(product_digits(0))     # 0