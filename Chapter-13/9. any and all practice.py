# any and all function

def my_sum(*args):
    if all([ (type(arg)==int or type(arg)==float) for arg in args ]):
        total = 0
        for num in args:
            total+=num
        return total
    else:
        return 'Wrong Input!'
print(my_sum(1, 2.2, 3, 4.5, 5, 6))
print(my_sum(1, 2.2, 3, 4.5, 5, 6, 'Waqar', [1, 2, 3]))