# Important
# ye check krngy string empty hai ya ni agr string empty hugi tou return uga false or agr string empty ni
# hogi tou return huga true

name=""
if name:
    print("String is not empty")
else:
    print("String is empty")

name="Waqar"
if name:
    print("String is not empty")
else:
    print("String is empty")

# Basic use of checking string empty or not
name=input("enter your name: ")
name=name.strip() # removes spaces from left and right of string
if name:
    print(f"Your name is {name}")
else:
    print("you did'nt type anything")