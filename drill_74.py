def digit_sum_until_zero():

    N = int(input("Enter a number N: "))

    while True:

        if N == 0:
            break

        total = 0

        while N > 0:
            current_digit = N % 10
            total = total + current_digit
            N = N // 10

        print(total)

        N = int(input("Enter a number N: "))


digit_sum_until_zero()


