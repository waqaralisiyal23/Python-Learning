# THIS IS CHALLENGE

# define a function that take any no. of lists containing number
# [1,2,3], [4,5,6], [7,8,9]
# return average
# (1+4+7)/3, (2+5+8)/3, (3+6+9)/3

# Try to make this anonymous function in one line using lambda
# def avarage_finder(*args):
#     average = []
#     for pair in zip(*args):                  # *args because args is a tuple and to unpack tuple we use *args
#         average.append(sum(pair)/len(pair))
#     return average
# print(avarage_finder([1,2,3], [4,5,6], [7,8,9]))
avarage_finder = lambda *args : [sum(pair)/len(pair) for pair in zip(*args)]
print(avarage_finder([1,2,3], [4,5,6], [7,8,9]))