def count_characters(str1):
    nums=0
    for i in str1:
        for j in i:
            nums+=1
    return nums
str1=['###','###','###']
str2=['22222222','22222222']
print(count_characters(str1))
print(count_characters(str2))