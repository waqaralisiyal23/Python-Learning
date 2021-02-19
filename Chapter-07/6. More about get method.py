user = {'name': 'Waqar', 'age': 20}
# user.get('names')       # returns None because names key doesn't exists
# but we can override this None
print(user.get('names', 'Key Not Found!'))