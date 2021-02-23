'''
Exercise#01: Define Generator function that will take one number as argument and generate a sequence of even numbers
from 0 to that number
'''
def even_generator(n):
    for num in range(0, n+1, 2):
        yield(num)
for num in even_generator(10):
    print(num)