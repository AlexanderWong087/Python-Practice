S=input('Input a string: ')
def norepetition(string):
    characters=[]
    for i in range(len(string)):
        if string[i] in characters:
            continue
        else:
            characters+=string[i]
    return characters
print(''.join(map(str,norepetition(S))))