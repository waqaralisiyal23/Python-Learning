# You have to have a complete understanding of functions
# first class functions / closures
# then finally we will learn about decorators

def square(a):
    return a**2

s = square
print(s.__name__)                                           # square
print(square.__name__)                                  # square
print(s(7))                                             # 49