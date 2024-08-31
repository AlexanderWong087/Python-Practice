def secret_society(names):
    name=''
    for i in range(len(names)):
        name+=names[i][0]
    name=''.join(sorted(name))
    return name
names=["Adam", "Sarah", "Malcolm"]
print(secret_society(names))