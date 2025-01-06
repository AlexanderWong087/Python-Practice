def isogram(str1):
    letters=[]
    str1=str1.lower()
    for i in str1:
        if i not in letters:
            letters+=i
        else:
            return False
    return True
print(isogram('Algorism'))
print(isogram('PasSword'))
print(isogram('Consecutive'))