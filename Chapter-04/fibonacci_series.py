# Fibonacci Series: 0 1 1 2 3 5 8 13 21 34 ...

def print_fibonacci_series(n):
    a = 0                   # first number
    b = 1                  # second number
    if n==1:
        print(a)
    elif n==2:
        print(a, b)                     # a b -> 0 1
    else:
        print(a,b, end=' ')             # ends with a space not with a new line
        for i in range(n-2):
            c = a+b
            a = b
            b = c
            print(b, end=' ')

print_fibonacci_series(8)
