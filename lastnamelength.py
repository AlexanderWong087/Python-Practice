def last_name_lensort(names):
    names.sort(key=lambda x: (len(x.split()[-1]), x.split()[-1]))
    return names
sorted_names = last_name_lensort([
    "Jennifer Figueroa",
    "Heather Mcgee",
    "Amanda Schwartz",
    "Nicole Yoder",
    "Melissa Hoffman"
])

print(sorted_names)