def compress(str1):
    count=1
    compressed=[]
    for i in range(1,len(str1)):
        if str1[i]==str1[i-1]:
            count+=1
        else:
            compressed.append(str1[i-1])
            if  count>1:
                compressed.append(str(count))
            count=1
    compressed.append(str1[-1])
    if count>1:
        compressed.append(str(count))
    return ''.join(compressed)
print(compress("aaabbcccccaaa"))
print(compress( "aaabbbaaa" ))
