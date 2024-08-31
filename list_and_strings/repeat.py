def find_repeated_elements(arr):
    repeated_elements = []
    unique_elements = set()
    for element in arr:
        if element in unique_elements:
            repeated_elements.append(element)
        else:
            unique_elements.add(element)
    return set(repeated_elements)
input_array = input("Enter elements of the array (space-separated): ").split()
input_array = [int(element) for element in input_array]
repeated_elements = find_repeated_elements(input_array)
if len(repeated_elements) == 0:
    print("-1")
else:
    print("Repeated elements:", repeated_elements)