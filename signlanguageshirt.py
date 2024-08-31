def fooling(real, said, known):
    if real==said:
        return "You didn't fool your friend"
    for i in range(len(real)):
        if said[i]!=real[i]:
            if said[i] in known or real[i] in known:    
                return "You didn't fool your friend"
    return "You fooled your friend"
fake_word=input('Input the word you told him: ')
real_word=input('Input the word on the shirt: ')
letters=input('Input what letters your friends knows: ').split()
print(fooling(real_word,fake_word,letters))