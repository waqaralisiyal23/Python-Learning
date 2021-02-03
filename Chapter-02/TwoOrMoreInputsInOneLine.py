#   split() function use krngy srf split() use krngy tou do values ko space se separate krna prega pr agr
# split(",") comma de diya split mn tou phr comma se separate krngy
name,age=input("Enter your name and age: ").split()  #split() mn kuch ni hai tou space se separate krngy
print(name)
print(age)

name,age=input("Enter your name and age: ").split(",")  #ab comma se separate krngy
print(name)
print(age)