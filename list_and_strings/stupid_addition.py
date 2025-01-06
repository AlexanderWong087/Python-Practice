def stupid_addition(var1,var2):
    if isinstance(var1,str) and isinstance(var2,str):
        return ('"'+var1+var2+'"')
    elif not isinstance(var1,str) and not isinstance(var2,str):
        return str(var1+var2)
    else:
        return None
print(stupid_addition("1","2"))
print(stupid_addition(1,2))
print(stupid_addition("1",2))