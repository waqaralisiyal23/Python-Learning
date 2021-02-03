#Enter user name and print in reverse 
#Note try to print in two lines using String Formatting
#one way
# name=input("Enter your name: ")
# reverse=name[-1::-1] #or name[::-1]
# print(f"Reverse of your name is {reverse}")

#second way and in two lines
name=input("Enter your name: ")
print(f"Reverse of your name is {name[::-1]}")