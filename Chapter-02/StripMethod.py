name="   Waqar    "
dots="......"
print(name+dots)

#To remove left space from string
print(name.lstrip()+dots)

#To remove right space from string
print(name.rstrip()+dots)

# strip() method removes both right and left spaces
print(name.strip()+dots)  

#But it will not remove middle spaces
name="    Wa    qar    "
print(name.strip()+dots)

#To remove middle spaces we use replace method and replace spaces with nothing or anything which we want
print(name.replace(" ","")+dots)

