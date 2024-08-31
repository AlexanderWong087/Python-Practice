def find_largest_common_substring_length(string1, string2):
    max_length = 0
    for i in range(len(string1)):
        for j in range(i+1, len(string1)+1):
            substring=string1[i:j]
            if substring in string2 and len(substring)>max_length:
                max_length=len(substring)
    return max_length
string1=input("Enter the first string: ")
string2=input("Enter the second string: ")
length=find_largest_common_substring_length(string1, string2)
print("Length of the largest common substring:", length)