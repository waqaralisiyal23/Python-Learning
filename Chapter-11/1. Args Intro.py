# make flexible functions

# * operator
# * args

# We can pass no. of arguments to total function and * operator will create a tuple and store all arguments in that
def  total(*args):
    print(args)
    print(type(args))
    total = 0
    for num in args:
        total+=num
    return total

print(total(1, 2, 3, 4, 5))
