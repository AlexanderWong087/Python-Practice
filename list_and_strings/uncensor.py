def uncensor(str1,str2):
    vowels=list(str2)
    new_str=""
    for i in range(len(str1)):
        if str1[i]=="*":
            new_str+=vowels[0]
            vowels.pop(0)
        else:
            new_str+=str1[i]
    print(new_str)
uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo")
uncensor("abcd", "")
uncensor("*PP*RC*S*", "UEAE")