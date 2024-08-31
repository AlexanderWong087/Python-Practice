string1=input('Input a string: ')
string2=input('Input a string: ')
if len(string1)>len(string2):
    print(string2+string1+string2)
if len(string2)>len(string1):
    print(string1+string2+string1)