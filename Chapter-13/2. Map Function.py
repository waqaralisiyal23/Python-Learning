# map function

numbers = [1, 2, 3, 4]

# def square(a):
#     return a**2
# squares = list(map(square, numbers))
squares = list(map(lambda x:x**2, numbers))    # map function mn humne ek function or iterable pass kiya hai wo ek ek krke iterable 
# ka element uthayega or function mn pass krega
print(squares)

list_ = ['abc', 'abcd', 'abcde']
length = list(map(len, list_))
print(length)