# Exception Handling
# try except else finally

while True:
    try:
        age = int(input('Enter your age: '))
        break
    except ValueError:
        print('Maybe you entered string instead of number, try again')
    except:
        print('Unexpected error')

if age<18:
    print('You can\'t play this game')
else:
    print('You can play this game')