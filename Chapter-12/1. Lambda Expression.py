# Lambda Expression (Anonymous Function)

def add_function(a, b):
    return a+b

add = lambda a,b: a+b
print(add(2, 3))

multiply = lambda a,b: a*b
print(multiply(2, 3))

print(add_function)             # <function add_function at 0x00FF0810>
print(add)                            # <function <lambda> at 0x01058660>
print(multiply)                    # <function <lambda> at 0x010586A8>