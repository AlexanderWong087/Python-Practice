def censor(str1):
    str1=str1.split(' ')
    str2=''
    for i in range(len(str1)):
        if len(str1[i])>4:
            str2+=(' '+'*'*len(str1[i]))
        elif i==0:
            str2+=str1[i]
        else:
            str2+=(' '+str1[i])
    return str2
print(censor("The code is fourty"))
print(censor("Two plus three is five"))
print(censor("aaaa aaaaa 1234 12345"))