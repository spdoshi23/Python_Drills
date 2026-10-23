inventory = {
    "laptop": {"price": 50000, "stock": 5},
    "mouse": {"price": 500, "stock": 20},
    "keyboard": {"price": 1500, "stock": 10},
    "monitor": {"price": 12000, "stock": 3},
    "headphones": {"price": 2000, "stock": 0}
}

sales = [
    ("laptop", 2),
    ("mouse", 5),
    ("keyboard", 3),
    ("mouse", 4),
    ("monitor", 3),
    ("headphones", 2),
    ("tablet", 1),
    ("laptop", 1),
    ("keyboard", 2),
    ("mouse", 3)
]

total_sold = {}
revenue = {}
unavailable_products = set()
stock_warnings = set()

for product, quantity in sales:
    if product in total_sold:
        total_sold[product] = total_sold[product] + quantity 
    else:
        total_sold[product] = quantity

total_revenue = 0
for product in total_sold.keys():
    if product in inventory:
        revenue[product] = inventory[product]["price"] * total_sold[product]
        if total_sold[product] > inventory[product]["stock"]:
            stock_warnings.add(product)
        total = total + revenue[product]
    else:
        unavailable_products.add(product)

print(total_sold)
print(revenue)
print(unavailable_products)
print(stock_warnings)
print(total_revenue)




















