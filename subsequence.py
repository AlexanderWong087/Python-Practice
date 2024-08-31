str1=input('Input a string: ')
str2=input('Input a string: ')
length=0
for i in str1:
    if i in str2:
        if len(i)==1:
            length+=1
print(length)