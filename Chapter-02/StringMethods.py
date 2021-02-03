# len() function: tells the length of string and also counts spaces in string
# lower() method: Methods are called with dot and this method makes your string in small letters
# upper() method: This method makes your string in capital letters
# title() method: This method makes the first character capital and all other small in each word of your String
# count() method: Counts the specified character in your string 

print(len("Waqar"))
name="Waqar Ali Siyal" #len() function also counts the spaces
print(len(name))

name="WaQaR ALi sIYaL"
print(name.lower())

name="waQAR ali sIyal"
print(name.upper())

name="waQaR AlI siYAL"
print(name.title())

name="Waqar Ali Siyal"
print(name.count("a")) #only counts small a