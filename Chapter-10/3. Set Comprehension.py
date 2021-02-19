# Set Comprehension
# Create a set which contains squares of numbers from 1 to 10
squares = {k**2 for k in range(1, 11)}
print(squares)

names = ['Waqar', 'Usama', 'Ahmed']
# Create a set contains only first letter of each name in above list
first_letter_set = {name[0] for name in names}
print(first_letter_set)