def multiply_nums(*args):
    multiply = 1         # 0 ni rkhna wrna 0 se multiply huke koi bhi number 0 he ajyega
    for i in args:
        multiply*=i
    return multiply

# print(multiply_nums(2,3,4))
nums = [2,3,4]
print(multiply_nums(*nums))             # *nums list ko unpack krega