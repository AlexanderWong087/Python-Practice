def tuck_in(lst1, lst2):
    mid=len(lst1)//2
    return lst1[:mid]+lst2+lst1[mid:]
lst1=[1,10]
lst2=[2,3,4,5,6,7,8,9]
print(tuck_in(lst1,lst2))