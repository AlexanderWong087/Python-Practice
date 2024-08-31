a=input('Input a string: ')
for i in range(len(a)):
    if len(a)%2==1:
        if a.count(a[i])>len(a)/2+0.5:
            value=0
        else:
            value=1
    else:
        if a.count(a[i])>len(a)/2:
            value=0
        else:
            value=1
print(value)