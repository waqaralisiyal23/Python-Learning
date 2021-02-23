# Iterator vs Iterable

# Lists, Tuples and Strings are iterables
# Iterator pr ek he bar loop chla skte hain lekin iterable pr again and again loop chla skty hain

numbers = [1, 2, 3, 4]           # Iterable
squares = map(lambda x:x**2, numbers)     # Iterator
print(numbers)
print(squares)

# How for loop works in iterables
# for i in numbers:
#     print(i)
numbers_iter = iter(numbers)
print(next(numbers_iter))
print(next(numbers_iter))
print(next(numbers_iter))
print(next(numbers_iter))

# How for loop works in iterators
# for i in squares:
#     print(i)
# humein yahan pe iterator bnane ki need ni q ke ye ek iterator hai already hum direct next call kr skty hain
print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))