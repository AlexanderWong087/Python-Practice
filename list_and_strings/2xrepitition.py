list=input('Input a list of words: ').split()
repeated=0
for a in list:
    count=0
    for i in range(len(list)):
        if list[i]==a:
            count+=1
    if count==2:
        repeated+=1
print(repeated/2)