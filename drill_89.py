def count_digits(n):
    if n < 10:
        return 1
    else:
        return 1 + count_digits(n//10)



print(count_digits(12345)) 
print(count_digits(789)) 
print(count_digits(7)) 
print(count_digits(0)) 
   