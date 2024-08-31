String1=input('Input a string: ')
String2=input('Input a string: ')
def find_repeated_elements(arr):
    repeated_elements = []
    unique_elements = set()
    for element in arr:
        if element in unique_elements:
            repeated_elements.append(element)
        else:
            unique_elements.add(element)
    return set(repeated_elements)
String1_repeats=len(find_repeated_elements(String1))
String2_repeats=len(find_repeated_elements(String2))
operations=0
for a in String1:
    if a not in String2:
        operations+=1
for b in String2:
    if b not in String1:
        operations+=1
operations+=String1_repeats+String2_repeats
print(operations)