a = {1, 2, 3, 4, 5}
b = {4, 5, 6}
c = {5, 6, 7}

a.update(b)
a.difference_update(c)
a.add(8)
a.discard(1)

print(a)