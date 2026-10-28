try:
    balance = 5000
    withdraw = input("Enter amount you want to withdraw: ")
    withdraw = int(withdraw)
    valid = True
    if withdraw <= 0:
        valid = False
        print("Withdrawal amount must be positive.")
    elif withdraw > balance:
        valid = False
        print("Insufficient balance!")
except ValueError:
    print("Enter valid integer")
else:
    if valid:
        rem_balance= balance - withdraw
        print(rem_balance)
finally:
    print("Transaction attempt completed.")














