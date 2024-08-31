def is_subset(list1,list2):
    for i in range(list1):
        if list1[i] in list2:
            continue
        else:
            return False
    return True
list1=[3, 2, 5]
list2=[5, 3, 7, 9, 2]
print(is_subset(list1,list2))