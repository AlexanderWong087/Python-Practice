def longest_valid_parentheses(string):
    stack = [-1]
    max_length = 0
    max_substring = ""
    for i in range(len(string)):
        if string[i] == "(":
            stack.append(i)
        else:
            stack.pop()
            if len(stack) == 0:
                stack.append(i)
            else:
                length = i - stack[-1]
                if length > max_length:
                    max_length = length
                    max_substring = string[stack[-1] + 1: i + 1]
    return max_substring
string = input("Enter a string consisting of '(' and ')': ")
substring = longest_valid_parentheses(string)
if substring:
    print(substring)