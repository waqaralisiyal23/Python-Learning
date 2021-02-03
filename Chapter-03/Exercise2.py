# Exercise2: Watch Coco Movie
# Ask user's name and age if user's name start with (a or A) and age is above 10 then user can watch Coco movie
# other wise cant watch

name,age=input("Enter your name and age(separated by ,): ").split(",")
name=name.strip()
age=age.strip()
age=int(age)
if (name[0]=="a" or name[0]=="A") and age>10:
    print("you can watch Coco movie")
else:
    print("you cannot watch Coco movie")