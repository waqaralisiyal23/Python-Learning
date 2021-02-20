'''
Exercise#02: Define a function a which takes list of string as input and returns a list but in that list the first
letter of each word must be capital and if reverse_str = True then we have to reverse every word and then we have to make
first letter capital. Do this using **kwargs
'''
def func(list_, **kwargs):
    if kwargs.get('reverse_str'):
        return [name[::-1].title() for name in list_]
    return [name.title() for name in list_]

print(func(['waqar', 'usama', 'ahmed']))
print(func(['waqar', 'usama', 'ahmed'], reverse_str = True))

