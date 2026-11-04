amount = int(input("Enter order amount: "))

fee = "Delivery fee: ₹0" if amount>=500 else "Delivery fee: ₹50" 
print(fee)
