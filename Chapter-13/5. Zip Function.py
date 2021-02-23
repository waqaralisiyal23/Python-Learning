# Zip function

user_id = ['user1', 'user2', 'user3']
names = ['Waqar', 'Usama', 'Ahmed']

# ('user1', 'Waqar')

zip_output = list(zip(user_id, names))
print(zip_output)               # [('user1', 'Waqar'), ('user2', 'Usama'), ('user3', 'Ahmed')]

# [('user1', 'Waqar'), ('user2', 'Usama'), ('user3', 'Ahmed')] we can convert this type of list to dictionary
print(dict(zip_output))

# We can zip also more than 2 lists
last_names = ['Siyal', 'Shaikh', 'Ali']
print(list(zip(user_id, names, last_names)))

l1 = ['a', 'b', 'c', 'd']
l2 = [1, 2, 3]
print(list(zip(l1, l2)))           # jese he choti wali list khtm hugi zipping khtm hujyegi [('a', 1), ('b', 2), ('c', 3)]
