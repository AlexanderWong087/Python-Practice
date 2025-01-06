def count_consonants(input_str):
    consonants = "bcdfghjklmnpqrstvwxyz"
    str1=input_str.lower()
    count = 0
    for char in str1:
        if char in consonants:
            count += 1
    return count
def count_vowels(input_str):
    vowels = "aeiou"
    str1=input_str.lower()
    count = 0
    for char in str1:
        if char in vowels:
            count += 1
            
    return count

input_string1 = "Jameel  Saeb!"
input_string2="He|\o my fr*nd"
input_string3="Smithsonian"
consonant_count1 = count_consonants(input_string1)
vowel_count1 = count_vowels(input_string1)
consonant_count2 = count_consonants(input_string2)
vowel_count2 = count_vowels(input_string2)
consonant_count3 = count_consonants(input_string3)
vowel_count3 = count_vowels(input_string3)
print(consonant_count1)
print(vowel_count1)
print(consonant_count2)
print(vowel_count2)
print(consonant_count3)
print(vowel_count3)