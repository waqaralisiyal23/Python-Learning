# Sum of n natural numbers entered by user
n = input("Enter number for sum of n natural numbers: ")
n = int(n)
total = 0
i = 1
while i<=n:
    total+=i
    i+=1
print(f"Sum of first {n} natural numbers is {total}")

