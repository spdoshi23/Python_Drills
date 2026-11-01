inventory = {
    "Notebook": {"price": 50, "stock": 10},
    "Pen": {"price": 10, "stock": 25},
    "Bag": {"price": 800, "stock": 3},
    "Bottle": {"price": 150, "stock": 0},
    "Pencil": {"price": 5, "stock": 40}
}

low_stock = []
unavailable_products = set()
value = 0
for product, info in inventory.items():
    print(f"{product} - Price: {info["price"]}, Stock: {info["stock"]}")
    value = (info["price"] * info["stock"]) + value

    if info["stock"] < 5:
        low_stock.append(product)

    if info["stock"] == 0:
        unavailable_products.add(product)


print("Low stock products:")
for i in low_stock:
    print(i)
print("Total inventory value:", value)

try:
    product_name = input("Enter product name: ")
    quantity = int(input("Enter quantity of that product: "))
    valid = True
except ValueError:
    print("Error: Quantity must be a number!")
else:
    if product_name not in inventory:
        valid = False
        print("Error: Product does not exist!")
    elif quantity <= 0:
        valid = False
        print("Quantity must be greater than 0.")
    elif quantity > inventory[product_name]["stock"]:
        valid = False
        print("Insufficient stock!")

    if valid:
        bill = inventory[product_name]["price"] * quantity
        inventory[product_name]["stock"] = inventory[product_name]["stock"] - quantity

        unavailable_products = set()
        for product, info in inventory.items():
            if info["stock"] == 0:
                unavailable_products.add(product)
        print("Unavailable products:", unavailable_products)
        print("Total bill:",bill)
        print("Remaining stock of", product_name, "is", inventory[product_name]["stock"])

        
