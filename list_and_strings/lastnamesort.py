def last_name_lensort(names):
    return sorted(names, key=lambda name: (len(name.split()[-1]), name.split()[-1]))
print(last_name_lensort([
    "Jennifer Figueroa",
    "Heather Mcgee",
    "Amanda Schwartz",
    "Nicole Yoder",
    "Melissa Hoffman"
])) 