def count_lesser(n, d):
    last_digit = n % 10
    remaining = n // 10
    if n < 10:
        if d > n:
            return 1
        else:
            return 0
    elif last_digit < d:
        return 1 + count_lesser(remaining, d)
    elif last_digit > d:
        return count_lesser(remaining, d)
    elif last_digit == d:
        return count_lesser(remaining, d)

print(count_lesser(58342, 3)) 
print(count_lesser(122245, 2)) 
print(count_lesser(1111, 5))   
print(count_lesser(9876, 6))   
print(count_lesser(7, 3))      
print(count_lesser(0, 0))      
print(count_lesser(0, 5))  