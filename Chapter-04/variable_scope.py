x=5                     # Global Variable
def my_func():
    x=7                 # Local Variable
    return x
print(my_func())
print(x)

# Change value of global variable inside function
y=5
def func_two():
    global y
    y=7
    return y
print(func_two())
print(y)