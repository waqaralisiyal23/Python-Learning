# function with all parameters
# vary important to understand

# PADK

# parameters
# * args
# default parameters
# ** kwargs

def func(name, *args, age=0, **kwargs):
    print(name)
    print(args)
    print(age)
    print(kwargs)

func('Waqar', 1,2,3, age=20,  a=1, b=2)