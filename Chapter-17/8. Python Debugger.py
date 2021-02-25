import pdb                # import pdb module
# module - python file contains usefull classes and functions wrote by developer

# According to wikipedia - debugging is the process of finding and resolving bugs (defects or problems that prevent correct
# operation) within computer programs, software, or systems.

# Why debugging
# 1) Our program is not running and causing unexpected errors
# 2) Our program is working fine but not working the same way we want

# Steps for debugging
# 1) Set trace
# 2) Execute code line by line

pdb.set_trace()
name = input('Please type your name: ')
age = input('Please type your age: ')
print(f'Hello {name} your age is {age}')
age2 = age+5
print(f'{name} your will be {age2} in next five years')

# l - to see the current execution line
# c - mtlb ab or debugging ni krni code continue chlana hai
# 1 - mtlb hum quit krna chahte hain