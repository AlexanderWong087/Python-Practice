array=input('Input the numbers: ').split()
x=int(input('Input how many times to rotate: '))
def shift_list(list):
    shifted_list=list[-x:]+list[:-x]
    return shifted_list
print(shift_list(array))