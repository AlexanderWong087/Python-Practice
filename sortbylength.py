def sort_by_length(inputed_list):
    for i in range(len(inputed_list)):
        for j in range(len(inputed_list)-i-1):
            if len(str(inputed_list[j]))>len(str(inputed_list[j+1])):
                inputed_list[j],inputed_list[j+1]=inputed_list[j+1],inputed_list[j]
    return inputed_list
list1=[1, 54, 1, 2, 463, 2]
list2=[999, 421, 22, 990, 32]
list3=[9, 8, 7, 6, 5, 4, 31, 2, 1, 3]
print(sort_by_length(list1))
print(sort_by_length(list2))
print(sort_by_length(list3))