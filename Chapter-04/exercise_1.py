'''
Exercise#01: Define a function which takes two numbers as a input and return greater of two numbers
'''
def greater_of_two(num1, num2):
    if num1>num2:
        return num1
    return num2

num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
print(f'{greater_of_two(5,3)} is greater')