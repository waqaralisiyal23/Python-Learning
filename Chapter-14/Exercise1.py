'''
Exercise#01:

@calculate_time
def square_finder(n):
    return [i**2 for i in range(1, n+1)]

square_finder(1000)

Output:
Executing... square_finder
This function took {3} sec to run
'''

from functools import wraps
import time

def calculate_time(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print(f'Executing... {function.__name__}')
        t1 = time.time()
        returned_value = function(*args, **kwargs)
        t2 = time.time()
        print(f'This function took {t2-t1} sec to run')
        return returned_value
    return wrapper

@calculate_time
def square_finder(n):
    return [i**2 for i in range(1, n+1)]

square_finder(1000000)