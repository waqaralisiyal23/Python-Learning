# We will do reverse in part2
# l1 = [1, 3, 5, 7]
# l2 = [2, 4, 6, 8]

l = [(1,2), (3,4), (5,6), (7,8)]

# * operator with zip
l1, l2 = list(zip(*l))
print(l1)               # tuple
print(l2)               # tuple
l1 = list(l1)
l2 = list(l2)
new_list = []
for pair in zip(l1,l2):
    new_list.append(max(pair))
print(new_list)
