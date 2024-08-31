def correct_stream(user_typed, correct):
    result=[]
    for i in range(len(user_typed)):
        if user_typed[i]==correct[i]:
            result.append(1)
        else:
            result.append(-1)
    return result

print(correct_stream(["cat", "blue", "skt", "umbrells", "paddy"], ["cat", "blue", "sky", "umbrella", "paddy"]))  # Output: [1, 1, -1, -1, 1]
print(correct_stream(["it", "is", "find"], ["it", "is", "fine"]))  # Output: [1, 1, -1]
print(correct_stream(["april", "showrs", "bring", "may", "flowers"], ["april", "showers", "bring", "may", "flowers"]))  # Output: [1, -1, 1, 1, 1]