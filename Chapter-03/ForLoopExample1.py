# sum of first ten natural numbers
total=0
for i in range(1,11):   # for sum of 20 numbers range(1,21)
    total+=i
print(f"Sum of first ten natural numbers is {total}")

# Sum of n natural numbers
n=input("Enter the number: ")
n=int(n)
total=0
for i in range(1,n+1):  # Second argument is excluded so to reach n we give n+1
    total+=i
print(f"Sum of first {n} natural numbers is {total}")
