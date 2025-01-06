def removeLetters(arr, txt):
    for char in txt:
        if char in arr:
            arr.remove(char)
    return arr
print(removeLetters(["s", "t", "r", "i", "n", "g", "w"], "string"))
print(removeLetters(["b", "b", "l", "l", "g", "n", "o", "a", "w"], "balloon"))
print(removeLetters(["d", "b", "t", "e", "a", "i"], "edabit"))