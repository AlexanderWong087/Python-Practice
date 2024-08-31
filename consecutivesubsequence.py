def findlongestConseqSubseq(arr,n):
    length=1
    maxlength=0
    for i in range(n):
        arr[i]=int(arr[i])
    arr.sort()
    for j in range(1,n):
        print(arr[j-1],arr[j])
        if arr[j]==1+arr[j-1]:
            length+=1
        else:
            length=1
        maxlength=max(maxlength,length)
    return maxlength
array=input('Input an array: ').split()
x=len(array)
result=findlongestConseqSubseq(array, x)
print(result)