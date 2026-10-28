try:
    balance =input("Enter your account balannce: ")
    withdraw = input("Enter amount you want to withdraw: ")
    balance = int(balance)
    withdraw = int(withdraw)
    if balance < 0:
        print("Balance cannot be negative!")
    elif withdraw <= 0:
        print("Withdrawal amount must be positive!")
    elif withdraw > balance:
        print("Insufficient balance!")
    else:
        rem_balance = balance - withdraw
        print("Withdrawal successful!")
        print(f"Remaining balance: {rem_balance}")
except ValueError:
    print("Invalid input! Enter whole numbers only.")


