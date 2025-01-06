def next_letter(str1):
    letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    new_str=''
    for i in str1:
        index1=letters.index(i)
        new_str+=letters[index1+1]
    return new_str
print(next_letter("hello"))
print(next_letter("bye"))
print(next_letter("welcome"))