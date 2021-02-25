# else and finally clause in exception handling

while True:
    try:
        number = int(input('Enter a number: '))
    except ValueError:
        print('Please type integer!!!')
    except:
        print('Unexpected error!!!')
    else:
        # agr koi exception na hui tou chlta hai else wala block yani agr try successfully chl gya tou else chlega
        print(f'User Input = {number}')
        break
    finally:
        # finally block chlta he chlta hai chahe exception aye ya na aye
        print('finally block executed')
