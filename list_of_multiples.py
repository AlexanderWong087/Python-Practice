def list_of_multiples(num,length):
    output=[]
    for i in range(length):
        output.append(num*(i+1))
    return output
print(list_of_multiples(7, 5)) #[7, 14, 21, 28, 35] 
print(list_of_multiples(12, 10)) #[12, 24, 36, 48, 60, 72, 84, 96, 108, 120] 
print(list_of_multiples(17, 6)) #[17, 34, 51, 68, 85, 102] 