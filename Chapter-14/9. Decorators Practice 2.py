from functools import wraps

def only_int_allow(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        if all([ type(arg)==int for arg in args ]):
            return function(*args, **kwargs)
        return 'Invalid Arguments!'
    return wrapper

@only_int_allow
def add_all(*args):
    total = 0
    for i in args:
        total+=i
    return total

print(add_all(1,2,3,4,5))
print(add_all(1,2,3,4,5, [1,2,3]))