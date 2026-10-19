def count_greater(n, d):
    last_digit = n % 10
    remaining = n // 10
    if n < 10:
        if n > d:
            return 1
        else:
            return 0
    elif last_digit > d:
        return 1 + count_greater(remaining, d)
    elif last_digit < d:
        return count_greater(remaining, d)
    elif last_digit == d:
        return count_greater(remaining, d)

print(count_greater(58342, 3)) 
print(count_greater(122245, 2)) 
print(count_greater(1111, 5))   
print(count_greater(9876, 6))   
print(count_greater(7, 3))      
print(count_greater(0, 0))      