def move_zeros(lst):
    zeros = [x for x in lst if x == 0]
    non_zeros = [x for x in lst if x != 0]
    return non_zeros+zeros

print(move_zeros([1, 0, 1, 2, 0, 1, 3])) 
print(move_zeros([0, 1, None, 2, False, 1, 0]))
print(move_zeros(['a', 0, 0, 'b', 'c', 'd', 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))