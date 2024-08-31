X=input('Input a string: ')
Y=input('Input a string: ')
def supersequence(x,y,m,n):
    supersequence=[]
    for i in range(m):
        if x[i] not in supersequence:
            supersequence+=x[i]
    for j in range(n):
        if y[j] not in supersequence:
            supersequence+=x[j]
    print(len(supersequence))    
supersequence(X,Y,len(X),len(Y))