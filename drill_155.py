inventory = {
    "Notebook": {"price": 50, "stock": 10},
    "Pen": {"price": 10, "stock": 25},
    "Bag": {"price": 800, "stock": 5}
}

product_name = input("Enter product name: ")
quantity = int(input("Enter quantity of that product: "))

if product_name not in inventory:
    raise ValueError ("Product not found")
elif quantity <= 0:
    raise ValueError ("Quantity must be positive")
elif quantity > inventory[product_name]["stock"]:
    raise ValueError ("Insufficient stock")
else:
    total = inventory[product_name]["price"] * quantity
    inventory[product_name]["stock"] = inventory[product_name]["stock"] - quantity
    print(total)
    print(inventory[product_name]["stock"])

