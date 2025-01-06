def longest_word(str1):
    str1=str1.split(' ')
    longest_word=''
    longest_word=str1[0]
    for i in range(len(str1)):
        if len(str1[i])>len(longest_word):
            longest_word=str1[i]
    return longest_word
print(longest_word("Margaret's toy is a pretty doll."))
print(longest_word("A thing of beauty is a joy forever."))
print(longest_word("Forgetfulness is by all means powerless!"))