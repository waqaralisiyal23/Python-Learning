# List Comprehension
# With the help of list comprehension we can create of list in one line

# Create a list of squares from 1 to 10
# squares = []
# for i in range(1, 11):
#     squares.append(i**2)
# print(squares)
squares = [i**2 for i in range(1, 11)]
print(squares)

# Create a list of negative numbers from 1 to 10
# negative = []
# for i in range(1, 11):
#     negative.append(-i)
# print(negative)
negative = [-i for i in range(1, 11)]
print(negative)

names = ['Waqar', 'Usama', 'Ahmed']
# Create a list which contains the first letter of each item in names list
# list_containing_first_letter = []
# for name in names:
#     list_containing_first_letter.append(name[0])
# print(list_containing_first_letter)
list_containing_first_letter = [name[0] for name in names]
print(list_containing_first_letter)