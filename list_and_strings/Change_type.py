def transform_list(lst):
    transformed_list = []
    for item in lst:
        if isinstance(item, bool):
            if item==False:
                transformed_list.append(True)
            else:
                transformed_list.append(False)
        elif isinstance(item, int) and item % 2 == 0:
            transformed_list.append(item + 1)
        elif isinstance(item, str):
            transformed_list.append(item.capitalize() + "!")
        else:
            transformed_list.append(item)
    return transformed_list
print(transform_list(["a", 12, True]))
print(transform_list([3, "13", "12", "twelve"]))
print(transform_list([False, "False", "true"]))