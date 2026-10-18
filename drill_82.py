def count_long_words(words):
    count = 0
    for i in words:
        if len(i) >= 5:
            count += 1
        else:
            continue
    return count

words = ["apple", "hi", "banana", "cat", "grapes", "dog"]
print(count_long_words(words))