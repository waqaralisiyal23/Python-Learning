# kwargs (keyword arguments)
# **kwargs (double * operator)

# kwargs as a parameter
def func(**kwargs):                     # ** operator converts the kwargs to dictionary
    print(kwargs)
    print(type(kwargs))
    for key,value in kwargs.items():
        print(f'{key} : {value}')

func(first_name = 'Waqar Ali', last_name = 'Siyal')

# dictionary unpacking
user_info = {'name': 'Waqar', 'age': 20}
func(**user_info)