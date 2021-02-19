numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Create a list from above list, if a number is odd then make it negative and if a number is even multiply it by 2
# Output should look like this: [-1, 4, -3, 8, -5, 12, -7, 16,-9, 20]
# new_list = []
# for num in numbers:
#     if num%2==0:
#         new_list.append(num*2)
#     else:
#         new_list.append(-num)
# print(new_list)
new_list = [num*2 if num%2==0 else -num for num in numbers]
print(new_list)
