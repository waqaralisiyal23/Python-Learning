# Filter function

# def is_even(num):
#     return num%2==0
numbers = [3,4,2,1,5,6,9,8,10]
# evens = tuple(filter(is_even, numbers))
evens = tuple(filter(lambda x:x%2==0, numbers))
print(evens)