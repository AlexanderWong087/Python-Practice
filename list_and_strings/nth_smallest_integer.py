def nth_smallest(lst, n):
    unique_sorted = sorted(set(lst))
    if n <= len(unique_sorted):
        return unique_sorted[n-1]
    else:
        return None
    
print(nth_smallest([1, 3, 5, 7], 1))
print(nth_smallest([1, 3, 5, 7], 3))
print(nth_smallest([1, 3, 5, 7], 5))
print(nth_smallest([7, 3, 5, 1], 2))