'''
Exercise#01
Define a function
Input -> num, iterable (tuple, list) containing numbers as args

example
nums = [1,2,3]
to_power(3, *nums)

output
list --> [1, 8, 27]

if user didn't pass any args then give user a message 'Hey! you didn't pass args'
else return list

Note: Use List Comprehension
'''
def to_power(power, *args):
    if args:               # means if args is not empty
        return [num**power for num in args]
    return 'Hey! you didn\'t pass args'

print(to_power(3, *[1,2,3]))