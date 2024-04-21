array=input('Input the array: ').split()
x=input('Input a value')
pairs=0
for i in range(len(array)):
    for j in range(len(array)):
        if i!=j and float(array[i])+float(array[j])==float(x):
            pairs+=1
print('Pairs found: ',pairs)        