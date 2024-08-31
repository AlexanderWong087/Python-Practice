def return_only_integer(list1):
    list2=[]
    for i in range(len(list1)):
        if isinstance(list1[i],int)==True:
            list2.append(list1[i])
    return list2
list1=[10, "121", 56, 20, "car", 3, "lion"]
print(return_only_integer(list1))