# Ask user a name and count each character of name
name=input("Enter your name: ")
name=name.strip()
name_copy=name.lower()
temp_var=""
for i in range(0,len(name)):
    if name_copy[i] not in temp_var:
        print(f"{name[i]} : {name_copy.count(name_copy[i])}")
        temp_var+=name_copy[i]