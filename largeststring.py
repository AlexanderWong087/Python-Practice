def largest_string(list1):
    longest_string=''
    for i in range(len(list1)):
        a=list1[i]
        if len(a)>len(longest_string):
            longest_string=a
    return longest_string
list1=['1','11','111','1111']
print(largest_string(list1))