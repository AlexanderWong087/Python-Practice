def find_leaders(arr):
    leaders = []
    max_right = float('-inf')
    for i in range(len(arr)-1, -1, -1):
        if arr[i] > max_right:
            leaders.append(arr[i])
            max_right = arr[i]
    leaders.reverse()
    return leaders
input_array = input("Enter the array: ")
input_array = list(map(int, input_array.split()))
result = find_leaders(input_array)
for j in range(len(result)):
    print(result[j],end=' ')