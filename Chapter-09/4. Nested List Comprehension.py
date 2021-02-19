example = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]

# Create a list same as above using nested list comprehension
# new_list = []
# for j in range(3):
#     new_list.append([1, 2, 3])
# print(new_list)
# nested_comp = [ [1, 2, 3] for i in range(3)]    # but also generate nested list using list comprehension
nested_comp = [ [i for i in range(1,4)] for j in range(3)]
print(nested_comp)