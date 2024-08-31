def move_zeros_to_end(arr):
    result=[]
    count_zeros=0
    for num in arr:
        if num!=0:
            result.append(num)
        else:
            count_zeros+=1
    result.extend([0]*count_zeros)
    return result
input_array = input("Enter the array elements separated by spaces: ")
array = list(map(int, input_array.split()))
result = move_zeros_to_end(array)
print(result)