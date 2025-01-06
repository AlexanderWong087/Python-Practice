def find_the_difference(str1, str2):
    lst1=list(str2)
    for ch in lst1:
        if ch in str1:
            lst1.remove(ch)
            str1 = str1.replace(ch, "", 1)
        else:
            return ch
print(find_the_difference("abcd", "abcde"))
print(find_the_difference("", "y"))
print(find_the_difference("ae", "aea"))