def multiply_nums(num, *args):
    multiply = 1         # 0 ni rkhna wrna 0 se multiply huke koi bhi number 0 he ajyega
    print(num)
    for i in args:
        multiply*=i
    return multiply

print(multiply_nums(9,2,4,5))          # 9 normal parameter hai wo multiply ni huga baki 2,4,5 *args hain