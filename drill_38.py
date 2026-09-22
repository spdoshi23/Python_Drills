N = int(input("Enter a number N: "))

original = N
most_count = 0

while N > 0:
    temp_digit = N % 10
    count = 0
    check = original

    while check > 0:
        current_digit = check % 10

        if current_digit == temp_digit:
            count = count + 1
        if count > most_count:
            most_count = count
            most_digit = temp_digit
        check = check // 10

    N = N // 10

print(most_digit)
















