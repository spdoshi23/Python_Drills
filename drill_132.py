inventory = {
    "pen": {"price": 10, "stock": 20},
    "notebook": {"price": 60, "stock": 5},
    "bag": {"price": 850, "stock": 3},
    "bottle": {"price": 250, "stock": 0},
    "pencil": {"price": 5, "stock": 0},
    "calculator": {"price": 600, "stock": 4}
}

product_value = {}
expensive_products  = {}
empty_stock = []

for product, details in inventory.items():
    product_value[product] = details["price"] * details["stock"]

    if details["price"] > 200:
        expensive_products[product] = details

    if details["stock"] == 0:
        empty_stock.append(product)

inventory_value = 0
for product, value in product_value.items():
    inventory_value = inventory_value + value

for i in empty_stock:
    inventory.pop(i)

print(product_value)
print(inventory_value)
print(inventory)
print(expensive_products)

































