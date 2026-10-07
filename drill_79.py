def count_vowels(words):
    vowel_count = 0
    i = 0
    while i < len(words):
        if words[i] == "":
            i = i+1
            continue
        elif words[i][0] in "aeiouAEIOU":
            vowel_count += 1
        i += 1
    return vowel_count

print(count_vowels(["apple", "Banana", "", "orange", "grape", "Umbrella"]))


















