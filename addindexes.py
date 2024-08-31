def add_index(list1):
    for i in range(len(list1)):
        list1[i]+=i
    return list1
list2=[5,4,3,2,1]
print(add_index(list2))