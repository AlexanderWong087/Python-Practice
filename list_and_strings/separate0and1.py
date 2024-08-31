array = input("Enter an array of 0s and 1s: ").split()
array = [int(num) for num in array]
new_array=[]


current_index=0
for i in range(len(array)):
    if array[current_index]==1:
        popped_elemnt = array.pop(current_index)
        array.append(popped_elemnt)
    else:
        current_index+=1
    
print(array)