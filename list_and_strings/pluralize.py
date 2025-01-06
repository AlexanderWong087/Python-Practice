def pluralize(words):
    from collections import Counter
    word_counts = Counter(words)
    result = set()
    for word, count in word_counts.items():
        if count > 1:
            result.add(word + 's')
        else:
            result.add(word)
    return result

print(pluralize(["cow", "pig", "cow", "cow"]))
print(pluralize(["table", "table", "table"]))
print(pluralize(["chair", "pencil", "arm"]))