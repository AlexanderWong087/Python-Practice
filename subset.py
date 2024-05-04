def isSubset():
    a1=input('Input array 1: ').split()
    a2=input('Input array 2: ').split()
    for i in range(len(a2)):
        if a2[i] in a1:
            continue
        else:
            print('Array 2 is not a subset of Array 1')
            return 'no'
    return 'yes'
print(isSubset())