def filter_names(names):
    result = []
    for i in names:
        if len(i) >= 4:
            result.append(i.upper())
        else:
            continue
    return result

names = ["raj", "Shubham", "aman", "Jo", "Kiran"]
print(filter_names(names))