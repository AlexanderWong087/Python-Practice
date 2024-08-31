results=input('Input the results of the match: ').split()
points=0
for i in range(10):
    x=results[i-1][0]
    y=results[i-1][2]
    if x>y:
        points+=3
    elif x==y:
        points+=1
print(points)