def filter_list(list1):
    list2=[]
    for i in range(len(list1)):
        if isinstance(list1[i],int)==True:
            list2.append(list1[i])
    return list2
list1=[1,2,"a","b"]
print(filter_list(list1))