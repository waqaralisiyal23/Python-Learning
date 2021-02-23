# List Comprehension
# squares = [i**2 for i in range(1,11)]
# print(squares)

# Generator Comprehension
squares = (i**2 for i in range(1,11))
for num in squares:
    print(num)
# Loop ek bar chla diya hai squares pr jo ke ek generator hai (iterator) tou dubara ni chla skty
for num in squares:
    print(num)