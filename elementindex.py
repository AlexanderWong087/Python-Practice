array1=input('Input an array: ').split()
array2=input('Input an array: ').split()
difference = []
index=0
for i in range (len(array1)):
    if array1[i]!=array2[i]:
        index=i
        break
print(index)