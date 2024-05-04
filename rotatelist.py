def rotate_list(list, d):
    rotated_list = list[d:] + list[:d]
    return rotated_list
array = input("Enter the list of numbers: ")
list = array.split()
d = int(input("Enter the number of elements to rotate: "))
rotated_lst = rotate_list(list, d)
print(rotated_lst)