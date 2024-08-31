def check(str1,str2,count):
    str1=str1.lower()
    str2=str2.lower()
    for a in range(len(str1)):
        if str1[a]==str2[a]:
            count+=1
    return count
string1=input('Input a string: ')
string2=input('Input a string: ')
repetitions=0
print(check(string1,string2,repetitions))