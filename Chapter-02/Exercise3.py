# Take two comma separated inputs from user
# 1) user's name 
# 2) a single character
# output: print 2 lines
# 1) user name's length 
# 2) count the character that user inputs (Bonus: case insensitive count) means character small hu ya cpital
# dono count kre

name,char=input("Enter name and character: ").split(",")
print(f"Length of your name is {len(name.strip())}")
print(f"Character count: {name.strip().lower().count(char.strip().lower())}") 
# name r char ko small krke us mn count kr rhy hain capital r small dono characters ka count miljyega 