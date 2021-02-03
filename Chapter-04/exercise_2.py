'''
Exercise#02: Define is_palindrome function that take one word in string as input and return True if it is 
palindrome else return False
palindrome - word that reads same backwards as forwards

Example:
is_palindrome('madam')                   -> True
is_palindrome('naman')                    -> True
is_palindrome('horse')                      -> False

Logic (Algorithm)
-> Reverse the string and compare reversed string with original string
'''

def is_palindrome(text):
    return text==text[ : :-1]
print(is_palindrome('madam'))
print(is_palindrome('naman'))
print(is_palindrome('horse'))