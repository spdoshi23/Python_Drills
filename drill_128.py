inventory = {
    "pen": 20,
    "book": 5,
    "pencil": 0,
    "eraser": 12,
    "ruler": 0
}

inventory.pop("pencil")

if "notebook" in inventory:
    pass
else:
    inventory["notebook"] = 10

print(inventory.get("book", 0))
print(inventory)
























