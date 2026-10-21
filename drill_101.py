numbers = [2, 5, 3, 2, 7, 5, 8, 3, 3]

seen = []
duplicate = []

for i in numbers:
    if i in seen:
        duplicate.append(i)
    else:
        seen.append(i)

print(set(duplicate))