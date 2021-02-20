# Lambda Expression Practice

def is_even(num):
    return num%2==0
print(is_even(5))

is_even2 = lambda num: num%2==0
print(is_even2(8))


def last_char(string_):
    return string_[-1]
print(last_char('waqar'))

last_char2 = lambda s:s[-1]
print(last_char2('ahmed'))


# Lambda expression with if else
def func(s):
    if len(s)>5:
        return True
    else:
        return False
print(func('waqar'))

func2 = lambda s : True if len(s)>5 else False
print(func2('abcdef'))

