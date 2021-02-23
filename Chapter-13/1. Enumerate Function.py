# We use enumerate function with for loop to track position of our item in iterable

names = ['Waqar', 'Usama', 'Ahmed']
# 0 --> Waqar
# 1 --> Usama
# 2 --> Ahmed
# How we can do this without enumerate function
pos = 0
for name in names:
    print(f'{pos} --> {name}')
    pos+=1
# with enumerate function
for pos, name in enumerate(names):
    print(f'{pos} --> {name}')

# Define a function that take two arguments
# 1) list containing string
# 2) string that want to find in your list
# and this function will return the index of string in your list and if string is not present then return -1
def find_pos(list_, target):
    for pos, item in enumerate(list_):
        if item==target:
            return pos
    return -1
print(find_pos(names, 'Usama'))