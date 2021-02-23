# def decorator_function(any_function):
#     def wrapper_function(*args, **kwargs):
#         '''This is wrapper function'''
#         print('This is awesome function')
#         return any_function(*args, **kwargs)
#     return wrapper_function

# @decorator_function
# def add(a,b):
#     '''This is add function'''
#     return a+b

# print(add(2, 3))
# print(add.__doc__)                      # This is wrapper function
# print(add.__name__)                   # wrapper_function

from functools import wraps

def decorator_function(any_function):
    @wraps(any_function)
    def wrapper_function(*args, **kwargs):
        '''This is wrapper function'''
        print('This is awesome function')
        return any_function(*args, **kwargs)
    return wrapper_function

@decorator_function
def add(a,b):
    '''This is add function'''
    return a+b

print(add(2, 3))
print(add.__doc__)                      # This is add function
print(add.__name__)                   # add