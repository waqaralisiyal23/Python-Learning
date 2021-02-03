# previous method which can be used in other programming languages
name="Waqar"
for i in range(len(name)):
    print(name[i])

# But now the method which we will use is used only in python
# In python strings are iterable
name="Waqar"
for i in name:
    print(i)
# sum of digits by this logic
num=input("Enter a number: ")
total=0
for i in num:
    total+=int(i)
print(total) 