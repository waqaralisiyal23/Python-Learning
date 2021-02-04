# function returning two values

def func(int1, int2):
    add = int1+int2
    multiply = int1*int2
    return add, multiply

add, multiply = func(2,3)         # first value stored in add and second value stored in multiply
print(add, multiply)                # 5 6
# but if we get multiple values in single variable then that will be a tuple
values = func(2,3)
print(values)                   # (5, 6)    which is a tuple
print(type(values))         # <class 'tuple'>
