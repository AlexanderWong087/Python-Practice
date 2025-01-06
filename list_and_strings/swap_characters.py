def double_swap(str1,c1,c2):
    characters=['']
    for i in str1:
        if i==c1:
            characters.append(c2)
        elif i==c2:
            characters.append(c1)
        else:
            characters.append(i)
    return ("".join(characters))
print(double_swap("aabbccc", "a", "b"))
print(double_swap("random w#rds writt&n h&r&", "#", "&"))
print(double_swap("128 895 556 788 999", "8", "9"))