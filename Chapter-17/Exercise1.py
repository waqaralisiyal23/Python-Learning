'''
Exercise#01: Make a function divide which takes two parameters a and b. Handle two excetions ZeroDivisionError
and TypeError.
'''
def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError as err:
        # return 'Please don\'t divide by zero'
        return err
    except TypeError as err:
        # return 'Please input numbers only'
        return err
    except:
        return 'Unexpected Error!!!'

print(divide(10,0))
print(divide(10, '4'))