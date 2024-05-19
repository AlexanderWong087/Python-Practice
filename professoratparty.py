array=input('Input the colors/numbers: ').split()
N=len(array)-1
new_array=[]
for i in range(N-1):
    new_array+=array[i]
    array.remove(array[i])
    for a in new_array:
        if a in array:
            print('Its a boys party')
            exit()
print('Its a girls party')
