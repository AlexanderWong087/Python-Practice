def get_missing_letters(str1):
    missing=[]
    letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in letters:
        if i not in str1:
            missing.append(i)
    missing.sort()
    missing=''.join(missing)

    return missing
print(get_missing_letters("abcdefgpqrstuvwxyz"))
print(get_missing_letters("zyxwvutsrq"))
print(get_missing_letters("abc"))
print(get_missing_letters("abcdefghijklmnopqrstuvwxyz"))