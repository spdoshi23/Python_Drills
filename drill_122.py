inventory = {
    "pen":  {"price": 10, "stock": 15},
    "book": {"price": 50, "stock": 8},
    "eraser": {"price": 5, "stock": 20},
    "ruler": {"price": 15, "stock": 4},
    "pencil": {"price": 5, "stock": 0}
}

inventory_value = {}
out_of_stock = set()
low_stock = set()

for item, detail in inventory.items():
    value = detail["price"]*detail["stock"]
    inventory_value[item] = value 

    if detail["stock"] == 0:
        out_of_stock.add(item)

    if 1 <= detail["stock"] <= 10:
        low_stock.add(item)

total_value = 0
for value in inventory_value:
    total_value = total_value + inventory_value[value]

print(inventory_value)
print(out_of_stock)
print(low_stock)
print(total_value)




























