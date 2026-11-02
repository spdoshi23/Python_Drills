account = {
    "name": "Alex",
    "balance": 5000
}

try:
    withdraw = input("Enter withdraw amount:")
    withdraw = int(withdraw)
    if withdraw <= 0:
        raise ValueError ("Withdrawal amount must be positive")
    elif withdraw > account["balance"]:
        raise ValueError ("Insufficient balance")
except ValueError as e:
    print(e)
else:
    print(withdraw, "rupees withrawn from account")
    account["balance"] = account["balance"] - withdraw
    print(account["balance"])
finally:
    print("ATM session ended")