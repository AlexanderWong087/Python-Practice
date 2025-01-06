def is_anagram(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    str1_dict={}
    str2_dict={}
    for i in str1:
        if i in str1_dict:
            
print(is_anagram("cristian", "Cristina"))
print(is_anagram("Dave Barry", "Ray Adverb"))
print(is_anagram("Nope", "Note"))
print(is_anagram("Sillent",'Listeen'))