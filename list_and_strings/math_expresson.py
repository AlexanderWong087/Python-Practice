def is_math_expr(input_str):
    allowed_chars = "0123456789()+-*/ "
    for char in input_str:
        if char not in allowed_chars:
            return False
    return True

print(is_math_expr("4 + 5"))
print(is_math_expr("4*6"))
print(is_math_expr("4*no"))