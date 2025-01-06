def parse_code(encoded_str):
    parts = list(filter(None, encoded_str.split('0')))
    return {
        "first_name": parts[0],
        "last_name": parts[1],
        "id": parts[2]
    }
print(parse_code("John000Doe000123"))
print(parse_code("michael0smith004331"))
print(parse_code("Thomas00LEE0000043"))