set_ = {'a', 'b', 'c'}

if 'a' in set_:
    print('a is present')
else:
    print('a is not present')

for item in set_:
    print(item, end='  ')
print()    # just for changing line

s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

# Union |
union_set = s1 | s2
print(union_set)

# Intersection &
intersection_set = s1 & s2
print(intersection_set)
