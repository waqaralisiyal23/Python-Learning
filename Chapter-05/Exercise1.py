'''
Exercise#01: Define a function which will take list containing numbers as input and return list containing
square of every element
'''

def square_list(list):
    squares = []
    for item in list:
        squares.append(item**2)
    return squares

print(square_list([1, 2, 3, 4, 5, 6, 7, 8, 9]))