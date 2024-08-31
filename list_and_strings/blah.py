import random
moves=input('Input 2 letters, R, P, or S: ')
A=moves[0]
B=moves[1]
if A==B:
    print('Draw')
elif (A=='R' and B=='S') or (A=='P' and B=='R') or (A=='S' and B=='P'):
    print('Player A wins')
else:
    print('Player B wins')