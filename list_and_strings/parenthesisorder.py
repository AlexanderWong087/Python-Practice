a=input('Input a string: ')
left_p=a.count('(')
right_p=a.count(')')
left_b=a.count('[')
right_b=a.count(']')
left_cb=a.count('{')
right_cb=a.count('}')
value='--'
if left_p==right_p and left_b==right_b and left_cb==right_cb:
    for i in range(len(a)):
        if a[i]=='(':
            if a.count(')',i)>1:
                value='true'
            else:
                value='false'
        elif a[i]=='[':
            if a.count(']',i)>1:
                value='true'
            else:
                value='false'
        elif a[i]=='{':
            if a.count('}',i)>1:
                value='true'
            else:
                value='false'
else:
    value='false'
print(value)