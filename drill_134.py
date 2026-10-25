sales = {
    "pen": {"price": 10, "sold": 50},
    "notebook": {"price": 60, "sold": 20},
    "bag": {"price": 850, "sold": 4},
    "bottle": {"price": 250, "sold": 0},
    "pencil": {"price": 5, "sold": 100},
    "calculator": {"price": 600, "sold": 3}
}

revenue = {}
successful_products = {}
zero_sold = []

for product, details in sales.items():
    revenue[product] = details["price"] * details["sold"]

    if revenue[product] >= 1000 and details["sold"] > 0:
        successful_products[product] = details

    if details["sold"] == 0:
        zero_sold.append(product)

total_revenue = 0
for product, amount in revenue.items():
    total_revenue = total_revenue + amount

for i in zero_sold:
    sales.pop(i)

print(sales)
print(revenue)
print(successful_products)
print(total_revenue)

























