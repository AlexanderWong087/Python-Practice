input=input('Input a string of 0s and 1s: ')
index=-1
for i in range(len(input)):
    if input[i]=='1':
        index=i
if index>=0:
    print(index)
elif index==-1:
    print('-1')