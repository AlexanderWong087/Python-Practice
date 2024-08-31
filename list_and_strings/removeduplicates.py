def remove_duplicates(list1):
    set1=[]
    for i in range(len(list1)):
        if list1[i] not in set1:
            set1.append(list1[i])
    return set1
list1=[1,3,3,5,5]
print(remove_duplicates(list1))