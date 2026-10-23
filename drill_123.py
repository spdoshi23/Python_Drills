words = [
    "python", "java", "python", "c++",
    "java", "python", "javascript", "c++",
    "java", "python"
]

frequency = {}
unique_word = set()
repeated_words = set()
most_common = None
most_appeared = 0

for i in words:
    if i in frequency:
        frequency[i] = frequency[i] + 1
    else:
        frequency[i] = 1
    
    if i in unique_word:
        repeated_words.add(i)
        unique_word.discard(i)
    elif i not in repeated_words:
        unique_word.add(i)

    if words.count(i) >= most_appeared:
        most_common = i
        most_appeared = words.count(i)

print(frequency)
print(unique_word)
print(repeated_words)
print(most_common)


























