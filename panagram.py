lowercase=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
indexes=[]
all_letteres=True
sentence=input('Input a string: ')
sentence=sentence.lower()
for i in range(25):
    if lowercase[i] in sentence:
        continue
    else:
        all_leters=False
if all_letteres==True:
    print('It is a panagram')
else:
    print('It is not a panagram')