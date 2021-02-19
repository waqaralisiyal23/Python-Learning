numbers = list(range(1, 11))
# print(numbers)           # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Create a list from above list which contains even numbers from 1 to 10 and also create without using above list
# do same for odd numbers
# even_nums = []
# for num in numbers:
#     if num%2==0:
#         even_nums.append(num)
# print(even_nums)
even_nums = [num for num in numbers if num%2==0]
even_nums_2 = [num for num in range(1, 11) if num%2==0]
print(even_nums, even_nums_2)

odd_nums = [num for num in numbers if num%2!=0]
odd_nums_2 = [num for num in range(1, 11) if num%2!=0]
print(odd_nums, odd_nums_2)