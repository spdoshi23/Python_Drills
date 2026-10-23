prices = {
    "pen": 10,
    "book": 50,
    "pencil": 5,
    "eraser": 8,
    "ruler": 15
}

cart = [
    "pen", "book", "pen", "pencil",
    "book", "pen", "eraser", "notebook",
    "pencil", "book"
]

item_count = {}
bill = {}
unavailable = set()

for items in cart:
    if items in item_count:
        item_count[items] = item_count[items] + 1
    else:
        item_count[items] = 1

    if items in prices:
        bill[items] = item_count[items] * prices[items]
    else:
        unavailable.add(items)

total_bill = sum(bill.values())






print(item_count)
print(bill)
print(unavailable)
print(total_bill)




























