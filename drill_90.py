def count_digits(n):
    if n < 10:
        return 1
    else:
        return 1 + count_digits(n//10)
    
def reverse_digit(n):
    if n < 10:
        return n

    last_digit = n % 10
    remaining = n // 10

    return last_digit * (10 ** count_digits(remaining)) + reverse_digit(remaining)

print(reverse_digit(1234))  
print(reverse_digit(56824))  
print(reverse_digit(6492))  
print(reverse_digit(5)) 
