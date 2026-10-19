def count_digits(n):
    if n < 10:
        return 1
    else:
        return 1 + count_digits(n//10)

def reverse_digit(n):
    last_digit = n % 10
    remaining = n // 10
    if n < 10:
        return n
    else:
        return last_digit * (10 ** count_digits(remaining)) + reverse_digit(remaining)

def is_palindrome(n):
    if n == reverse_digit(n):
        return True
    else:
        return False

print(is_palindrome(121))    # True
print(is_palindrome(1331))   # True
print(is_palindrome(1234))   # False
print(is_palindrome(7))      # True
print(is_palindrome(1221))   # True
print(is_palindrome(12321))  # True
print(is_palindrome(10))     # False

    