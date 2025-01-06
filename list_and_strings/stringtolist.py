def stringtolist(str1):
    lst1=[]
    last_word_start=0
    word=''
    for i in range(len(str1)):
        if last_word_start==0 and str1[i]==" ":
            word=str1[0:i]
            last_word_start=i
            lst1.append(word)
        elif str1[i]==" ":
            word=str1[last_word_start+1:i]
            last_word_start=i
            lst1.append(word)
        elif i==len(str1)-1:
            word=str1[last_word_start+1:i+1]
            lst1.append(word)
        if " " not in str1:
            return [str1]
    return lst1
print(stringtolist('Hello'))
