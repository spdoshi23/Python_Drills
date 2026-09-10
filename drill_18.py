def count_vowels(text):
    count = 0
    for character in text:
        if character in("aeiouAEIOU"):         #dont forget to quote vowel string
            count = count + 1
    return count

x = count_vowels("Bengaluru")
print(f"Total vovels: {x}")
