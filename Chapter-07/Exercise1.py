'''
Exercise#01: Define a function that takes a number(n) and returns a dictionary containing cube of numbers from 1 to n
'''
def cube_finder(num):
    cubes = {}
    for i in range(1, num+1):
        cubes[i] = i**3
    return cubes
print(cube_finder(5))