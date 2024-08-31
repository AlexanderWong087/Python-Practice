def pos_neg_sort(lst): 
    positive_nums = sorted([x for x in lst if x > 0]) 
    result = [x if x <= 0 else positive_nums.pop(0) for x in lst] 
    return result 

 

print(pos_neg_sort([6, 3, -2, 5, -8, 2, -2])) 
print(pos_neg_sort([6, 5, 4, -1, 3, 2, -1, 1]))  
print(pos_neg_sort([-5, -5, -5, -5, 7, -5]))  