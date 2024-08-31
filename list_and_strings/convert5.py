def convert_zeros_to_fives(number):
    number_str = str(number)
    number_str = number_str.replace('0', '5')
    converted_number = int(number_str)
    return converted_number

input_number = int(input("Enter a number: "))
converted_number = convert_zeros_to_fives(input_number)
print(converted_number)