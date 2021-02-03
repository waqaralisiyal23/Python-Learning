#Syntax
# if condition:
#       code
#       if condition is true this code will execute

age = input("Enter your age: ")
age = int(age)
if age>=14:
    print("You are above 14")

if age>=18:
    print("You are eligible for vote.")
    print("**************************")     # multiple lines in if