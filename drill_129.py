inventory = {
    "pen": 20,
    "book": 5,
    "pencil": 0,
    "eraser": 12,
    "ruler": 0,
    "notebook": 8
}

zero_stock = []

for product, stock in inventory.items():
    if stock == 0:
        zero_stock.append(product)                              #we cant directly pop bcx by doing so, it will reduce dictionary's size, giving runtime error

for i in zero_stock:
    inventory.pop(i)

print(inventory)
























