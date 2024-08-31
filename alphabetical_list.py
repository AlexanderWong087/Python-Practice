def alphabetical_list(list1,n):
    result=sorted(list1,key=lambda x: x[n-1])
    return result
list1,n1=["az16", "by35", "cx24"], 2
list2,n2=["mayor", "apple", "petal"], 5
list3,n3=["mate", "team", "bade"], 3
print(alphabetical_list(list1,n1))
print(alphabetical_list(list2,n2))
print(alphabetical_list(list3,n3))