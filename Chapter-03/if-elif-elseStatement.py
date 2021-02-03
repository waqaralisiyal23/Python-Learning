# if-elif-else used for multiple conditions
#   Show ticket pricing based on age

age=input("enter your age: ")
age=int(age)
if age==0 or age<0:
    print("Invalid age")
elif 0<age<=3:
    print("Ticket price: Free")
elif 3<age<=10:
    print("Ticket price: 150")
elif 10<age<=60:
    print("Ticket price: 250")
else:
    print("Ticket price: 200")