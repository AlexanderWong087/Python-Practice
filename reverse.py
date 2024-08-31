def reverse(integer_list):
    new_list=[]
    for i in range(len(integer_list)):
        new_list.append(integer_list[-1*(i+1)])
    return new_list
list1=[1,2,3,4,5]
print(reverse(list1))