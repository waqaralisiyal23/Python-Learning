# how to add items to our list
# most common thing that you can do with your list and most important

fruits1 = ['grapes', 'apple']
fruits1.append('mango')                      # append method adds data to the end of the list
print(fruits1)

words = []
words.append('word1')
words.append('word2')
words.append('word3')
words.append('word4')
words.append('word5')
print(words)

# Some more methods to add data in our list
# insert method
fruits2 = ['banana', 'orange']
fruits2.insert(1, 'strawberries')                 # strawberries added at index 1 and other items will shift on step forward
print(fruits2)

# how to join (concatenate) two list
fruits = fruits1 + fruits2
print(fruits)

# extend method
fruits1.extend(fruits2)
print(fruits1)                          # output: ['grapes', 'apple', 'mango', 'banana', 'strawberries', 'orange']

# difference between append and extend method
# if we use fruits1.append(fruits2) then output will be
# ['grapes', 'apple', 'mango', ['banana', 'strawberries', 'orange']] which is list inside list