# Decorators - enhance the functionality of other functions
# @ use for decorators - known as syntactic sugar

# def func1():
#     print('This is function 1')

# def func2():
#     print('This is function 2')

# Ab ham chahte hain ke jab bhi hum func1 ko call krein ya phr func2 ko call krein tou phle print hu 'This is awesome function' or
# humein code bhi change ni krna hai func1 or func2 ka tou inki functionalities ko enhance krne ke liye hum use krengy decorator

def decorator_function(any_function):
    def wrapper_function():
        print('This is awesome function')
        any_function()
    return wrapper_function

# func1 = decorator_function(func1)
# func1()                # wrapper function executes
# func2 = decorator_function(func2)
# func2()                # wrapper function executes

@decorator_function                                     # shortcut to enhance functionality
def func1():
    print('This is function 1')

@decorator_function
def func2():
    print('This is function 2')

func1()
func2()

