string1="the sky is blue"
string2="hello world!"
string3="a good example"
def reverse_strings(str1):
    lst1=str1.split(' ')
    lst2=[]
    for i in range(len(lst1)):
        lst2.append(lst1[-1*(i+1)])
    return ' '.join(lst2)
print(reverse_strings(string1))
print(reverse_strings(string2))
print(reverse_strings(string3))