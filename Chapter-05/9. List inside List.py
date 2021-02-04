matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]                                          # 2d list
# matrix list has 3 items --> 3 lists
print(matrix[0])                                # [1, 2, 3]
print(matrix[1])                                # [4, 5, 6]
print(matrix[2])                                # [7, 8, 9]

# print all elements of 2d list
for sublist in matrix:
    for item in sublist:
        print(item)

# access any specific value in 2d list
print(matrix[0][1])                                   # prints: 2
print(matrix[2][0])                                   # prints: 7
