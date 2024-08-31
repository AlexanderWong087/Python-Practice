def index_filter(list1,string1):
    result=''
    for i in range(len(list1)):
        result+=string1[list1[i]]
    return result 
list1=[0, 1, 5, 7, 4, 2]
string1="Cry me a river"
print(index_filter(list1,string1))