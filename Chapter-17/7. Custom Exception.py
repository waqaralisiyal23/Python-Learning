# Custom Exceptions
# Q) Why custom exceptions?
# Ans) To inrease the readability of code

class NameTooShortError(ValueError):
    pass

def validate(name):
    if len(name)<8:
        raise NameTooShortError('Name is too short')

username = input('Enter your name: ')
validate(username)
print(f'Hello {username}')
