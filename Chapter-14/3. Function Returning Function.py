# Function Returning Function
def outer_func():
    def inner_func():
        print('Inside inner func')
    return inner_func
var = outer_func()
var()              # here var is a function because outer_func() returns a function

def outer_func2(msg):
    def inner_func2():
        print(f'Message is {msg}')
    return inner_func2
var2 = outer_func2('Hey!')
var2()