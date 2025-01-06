def scottish(str1):
    vowels='aeiou'
    new_str = ""
    for i in str1.lower():
        if i in vowels:
            new_str += 'e'
        else:
            new_str += i
    return new_str.upper()
print(scottish("hello world"))
print(scottish("Mr. Fox was very naughty"))
print(scottish("Butterflies are beautiful!"))
print(scottish("Alexander is Amazing!"))
mydict = {83:  80}
txt = "Hello Sam!"
print(txt.translate(mydict))
