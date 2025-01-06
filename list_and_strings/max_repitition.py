def max_adjacent_repeats(text: str, search: str) -> (int, int):
    max_count=0
    max_index=-1
    current_count=0
    current_index=-1
    search_length=len(search)
    i=0
    while i <= len(text) - search_length:
        if text[i:i + search_length] == search:
            if current_count == 0:
                current_index = i
            current_count += 1
            i += search_length
        else:
            if current_count > max_count:
                max_count = current_count
                max_index = current_index
            current_count = 0
            current_index = -1
            i += 1
    if current_count > max_count:
        max_count = current_count
        max_index = current_index
    
    return max_count, max_index

print(max_adjacent_repeats("abxxcabxaaaxcabxxxxc", "x"))  # Output: (4, 15)
print(max_adjacent_repeats("acababaxyzababababababdexayababababxyz", "ab"))  # Output: (6, 10)