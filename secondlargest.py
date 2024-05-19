array=input('Input an array: ').split()
for a in range(len(array)-1):
    array[a]=int(array[a])
for j in range(2):
    if j==1:
        array.remove(largest)
    largest=array[0]
    for i in range(1,len(array)-1):
        if array[i]>largest:
            largest=array[i]
print(largest)