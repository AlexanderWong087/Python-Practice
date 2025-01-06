def shared_characters(str1,str2):
    count=0
    for i in str1:
        if i in str2:
            count+=1
    return count
print(shared_characters("apple", "meaty"))
print(shared_characters("fan", "forsook"))
print(shared_characters("spout", "shout"))