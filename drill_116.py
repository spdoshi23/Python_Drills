items = ["pen", "book", "pen", "pencil", "book", "eraser", "pen"]

seen = set()
duplicate = set()
for i in items:
    if i in seen:
        duplicate.add(i)
    else:
        seen.add(i)

print(duplicate)






















