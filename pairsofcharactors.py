# S=input('Input a string: ')
# def string_pairs(string):
#     pairs=[]
#     if len(string)%2==0:
#         for i in range(len(string)):
#             pairs+=string[i]+string[2*i+1]
#     else:
#         if 2*i-1==len(string):
#             for i in range(len(string)-1):
#                 pairs+=string[2*i]+string[2*i+1]
#             pairs+=string[-1]+'*'
#         else:
#             for i in range(len(string)):
#                 pairs+=string[2*i]+string[2*i+1]
#     return pairs
# print(string_pairs(S))

def string_pairs(string):
    for i in range(0,len(string),2):
        print(i)



string_pairs("mubashir") # ["mu", "ba", "sh", "ir"]
            # 01234567