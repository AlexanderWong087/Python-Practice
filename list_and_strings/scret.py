def secret(code):
    parts = code.split('.')
    tag = parts[0]
    classes = ' '.join(parts[1:])
    return f"<{tag} class='{classes}'></{tag}>"
print(secret("p.one.two.three"))
print(secret("p.one"))
print(secret("p.four.five"))