t = (5, 10, 15)
a, b, c = t
print(a, b, c)
x = 10
y = 20
print(f"Before swapping: x = {x}, y = {y}")
x, y = y, x
print(f"After swapping: x = {x}, y = {y}")
t = (1, 2, 3, 4, 2, 5, 2)
index = t.index(2)
print(f"The index of the first occurrence of 2 is: {index}")
single_element_tuple = (10,)
print(f"The type of the single element tuple is: {type(single_element_tuple)}")