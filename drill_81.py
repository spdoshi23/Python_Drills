def filter_words(words):
    result = []
    for i in words:
        if len(i) >=4:
            result.append(i.lower())
        else:
            continue
    return result

words = ["Hi", "PYTHON", "Code", "AI", "LOOP"]
print(filter_words(words))