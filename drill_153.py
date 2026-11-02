account = {
    "name": "Alex",
    "balance": 5000
}

withdraw = int(input("Enter withdraw amount:"))
if withdraw <= 0:
    raise ValueError ("Withdrawal amount must be positive")
elif withdraw > account["balance"]:
    raise ValueError ("Insufficient balance")
else:
    rem_balance = account["balance"] - withdraw
    print(rem_balance)

