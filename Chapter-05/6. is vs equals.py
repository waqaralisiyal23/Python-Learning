# compare lists
# ==, is
# == check values inside list
# is checks address inside memory
fruits1 = ['orange', 'apple', 'pear']
fruits2 = ['banana', 'kiwi', 'apple']
fruits3 = ['orange', 'apple', 'pear']
print(fruits1==fruits2)                             # False
print(fruits1==fruits3)                             # True
print(fruits1 is fruits3)                             # False