import random
secret = random.randint(1, 100)

user_input = int(input("Guess the number:  "))
attempt = 0
if user_input == secret:
    print("YOU GUESSED THE SECRET NUMBER IN FIRST ATTEMPT")
else:
    while user_input != secret:
        attempt = attempt + 1
        if user_input > secret:
            print("Lower")
        elif user_input < secret:
            print("Higher")
        user_input = int(input("Guess the number:  "))
        if user_input == secret:
            print("YOU GUESSED THE SECRET NUMBER IN",attempt+1, "ATTEMPTS" )





























