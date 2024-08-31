def letter_range(range_str): 
    start,end = range_str.split('-') 
    start_ord,end_ord = ord(start),ord(end) 
    letters = [chr(i) for i in range(start_ord, end_ord + 1)] 
    return ''.join(letters) 

letters=input('Input the range: ') 
print(letter_range(letters)) 