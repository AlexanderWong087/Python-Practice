def digit_occurrences(num1,num2,digit):
    lst1=[]
    count=0
    for i in range(num1,num2+1):
        lst1.append(str(i))
    for a in lst1:
        count+=a.count(str(digit))
    return count
print(digit_occurrences(51, 55, 5))
print(digit_occurrences(1, 8, 9))
print(digit_occurrences(-8, -1, 8) )
print(digit_occurrences(71, 77, 2))