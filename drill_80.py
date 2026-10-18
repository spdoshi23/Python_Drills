def update_scores(scores):
    result = []
    for i in scores:
        if i >= 40:
            result.append(i*i)
        else:
            continue
    return result

scores = [20, 40, 50, 15, 60, 35]
print(update_scores(scores))
