string=input('Input a string: ')
newstring=string[0]
lowercase=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
uppercase=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
uppercase_condition=True
if string[0] in uppercase:
    uppercase_condition=True
else:
    uppercase_condition=False
for i in range(len(string)-1):
    if uppercase_condition==True:
        if (i+1)%2==0:
            newstring+=string[i+1].upper()
        else:
            newstring+=string[i+1].lower()
    else:
        if (i+1)%2==0:
            newstring+=string[i+1].lower()
        else:
            newstring+=string[i+1].upper()
print(newstring)