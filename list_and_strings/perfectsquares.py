N=int(input('Input a number: '))
squares=0
while True:
    if (squares+1)*(squares+1)<N:
        squares+=1
    else:
        break
print(squares)