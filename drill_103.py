numbers = [5, 2, 5, 8, 2, 9, 8, 1, 7, 7]

ans = set()
for i in numbers:
    if numbers.count(i) == 1:
        ans.add(i)

print(ans)











