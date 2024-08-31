def sort_by_letter(strings):
    def custom_key(s):
        sorted_letters = sorted([c for c in s if c.isalpha()])
        return ''.join(sorted_letters)
    return sorted(strings, key=custom_key)

result1 = sort_by_letter(["932c", "832u32", "2344b"])
print(result1)
result2 = sort_by_letter(["99a", "78b", "c2345", "11d"])
print(result2)
result3 = sort_by_letter(["572z", "5y5", "304q2"])
print(result3)
result4 = sort_by_letter([])
print(result4)