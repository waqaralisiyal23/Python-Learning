'''
Take a number from user (i.e 1256) then print sum of te digits
1+2+5+6 = total and print total
'''
num=input("Enter the number: ")
num=num.strip()
total=0
for i in range(len(num)):   # i from 0 to len(num)-1
    total+=int(num[i])
print(f"Sum of digits of a number is {total}")