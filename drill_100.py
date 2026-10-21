def first_repeated(items, seen):
    if not items:
        return None

    first = items[0]
    remaining = items[1:]

    if first in seen:
        return first
    else:
        seen.append(first)
        return first_repeated(remaining, seen)


print(first_repeated([3, 5, 2, 5, 3], []))  # 5
print(first_repeated([1, 2, 3, 4], []))     # None
print(first_repeated([7, 7, 8], []))        # 7
print(first_repeated([4, 1, 4, 1], []))     # 4
print(first_repeated([9], []))              # None
print(first_repeated([], []))               # None