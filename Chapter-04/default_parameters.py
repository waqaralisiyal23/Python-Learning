def example_one(num1, num2, num3 = 8):
    print(num1, num2, num3)
example_one(5,6)
example_one(8,3,4)

def user_info(first_name='unknown', last_name='unknown', age = None):
    print(f'Your first name is {first_name}')
    print(f'Your last name is {last_name}')
    print(f'Your age is {age}')
user_info()
user_info('Waqar Ali', 'Siyal', age=20)