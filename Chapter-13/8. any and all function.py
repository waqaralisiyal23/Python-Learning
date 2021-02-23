# any and all function
# any function - returns True if there is atleast one True in the list otherwise False
# all function - returns True if all values are True in the list otherwise False

numbers1 = [2, 4, 6, 8, 10]
numbers2 = [1, 2, 3, 4, 5, 6]

# evens1 = []
# for num in numbers1:
#     evens1.append(num%2==0)
# print(all(evens1))

print(all(num%2==0 for num in numbers1))
print(any(num%2==0 for num in numbers2))