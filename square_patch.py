def square_patch(n):
    if n<=0:
        return []
    square=[]
    for i in range(n):
        row=[n]*n
        square.append(row)
    return square

print(square_patch(3)) 
print(square_patch(5))