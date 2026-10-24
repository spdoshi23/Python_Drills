products = {
    "pen": 10,
    "notebook": 60,
    "bag": 850,
    "bottle": 250,
    "pencil": 5,
    "calculator": 600
}

expensive_products = {}

for product, price in products.items():
    if price > 200:
        expensive_products[product] = price

print(expensive_products)

total = 0
for product, price in expensive_products.items():
    total = total + price

print(total)






















