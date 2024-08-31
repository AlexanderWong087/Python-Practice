def increment(List_input, increment):
    for i in range(len(List_input)):
        List_input[i]=List_input[i]+increment
    return List_input
numbers=[1,2,3,4,5]
integer=int(input('Input an integer: '))
print(increment(numbers, integer))