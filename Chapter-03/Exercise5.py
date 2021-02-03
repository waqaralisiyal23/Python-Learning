# Ask a user for name(Example: Waqar Ali Siyal). Print count of each character with spaces
# Hint : use count method

name = input("enter your name: ")
name=name.strip().lower()
temp_var="" #is mn jo jo character count hoty jayngy unhe add krte jyngy 
i=0
while i<len(name):
    if name[i] not in temp_var:     #agr character temp_var mn ni hai phle count ni hua ahi tou chlega agy
        temp_var+=name[i]  # jo character count hujyega wo is mn ajyega
        print(f"{name[i]} : {name.count(name[i])}")
    i+=1  # ye increase while ki body mn ayega if se bahir