account = {
    "name": "Alex",
    "balance": 5000
}
try:
    withdraw = input("Enter withdraw amount:")
    withdraw = int(withdraw)
    valid = True
    if withdraw <= 0:
        valid = False
        print("Withdrawal amount should be greater than 0")
    elif withdraw > account["balance"]:
        valid = False
        print("Insufficient balance!")
except ValueError:
    print("Enter a valid integer")
else:
    if valid:
        rem_balance = account["balance"] - withdraw
        account["balance"] = rem_balance
        print(account)
finally:
    print("Transaction attempt completed.")

