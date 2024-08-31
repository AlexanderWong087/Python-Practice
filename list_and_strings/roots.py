import math
def check_square_and_cube(num1,num2):
    sqrt=math.sqrt(num1)
    if sqrt*sqrt*sqrt==num2:
        return 'yes'
    return 'no'
print(check_square_and_cube(4, 8), 
    check_square_and_cube(16, 48),
    check_square_and_cube(9, 27) )